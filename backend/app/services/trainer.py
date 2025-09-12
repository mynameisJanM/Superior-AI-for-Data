from ..models.incremental_trainer import IncrementalTrainer
from sqlalchemy.orm import Session
from random import sample

replay_buffer = []  # In-memory

def run_training(job_id: str, db: Session):
    global replay_buffer
    items = db.query(DataItem).filter(DataItem.soft_deleted == False).all()
    replay_buffer = [item.content for item in sample(items, min(10, len(items)))]  # Simple sample
    trainer = IncrementalTrainer()
    trainer.train(replay_buffer)  # Mock