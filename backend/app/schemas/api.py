from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime, timedelta
from .database import get_db
from .models.data_item import DataItem
from .models.train_job import TrainJob
from .models.audit_log import AuditLog
from .schemas.data_item import DataItemCreate
from .schemas.query import QueryRequest, QueryResponse
from .schemas.train import TrainStatus
from .schemas.prune import PruneRequest, PruneResponse
from .schemas.audit import AuditResponse
from .services.embedding import compute_embedding
from .services.vector_db import insert_vector, search_vectors, delete_vector
from .services.trainer import run_training
from .services.pruner import prune_data

router = APIRouter()

@router.post("/ingest")
def ingest(item: DataItemCreate, db: Session = Depends(get_db)):
    new_item = DataItem(id=str(uuid4()), content=item.content)
    db.add(new_item)
    db.commit()
    vector = compute_embedding(item.content)
    insert_vector(new_item.id, vector)  # Sync
    return {"id": new_item.id}

@router.post("/query")
def query(req: QueryRequest, db: Session = Depends(get_db)):
    results = search_vectors(req.text, top_k=5)
    return QueryResponse(matches=results)

@router.post("/train-request")
def request_train(db: Session = Depends(get_db)):
    job = TrainJob(id=str(uuid4()))
    db.add(job)
    db.commit()
    return {"job_id": job.id}

@router.post("/approve-train/{job_id}")
def approve_train(job_id: str, db: Session = Depends(get_db)):
    job = db.query(TrainJob).filter(TrainJob.id == job_id).first()
    if job:
        job.status = "approved"
        db.commit()
        run_training(job_id, db)  # Sync mock
    return {"status": "approved"}

@router.get("/train-status/{job_id}")
def get_status(job_id: str, db: Session = Depends(get_db)):
    job = db.query(TrainJob).filter(TrainJob.id == job_id).first()
    return TrainStatus(status=job.status if job else "not_found")

@router.post("/clear")
def clear(id: str, db: Session = Depends(get_db)):
    item = db.query(DataItem).filter(DataItem.id == id).first()
    if item:
        item.soft_deleted = True
        delete_vector(id)
        audit = AuditLog(action="clear", details={"id": id})
        db.add(audit)
        db.commit()
    return {"cleared": id}

@router.post("/prune")
def prune(req: PruneRequest, db: Session = Depends(get_db)):
    candidates = prune_data(db, req.dry_run)
    return PruneResponse(candidates=candidates)

@router.get("/audit")
def audit(db: Session = Depends(get_db)):
    logs = db.query(AuditLog).all()
    return AuditResponse(logs=[{"action": l.action, "timestamp": l.timestamp} for l in logs])