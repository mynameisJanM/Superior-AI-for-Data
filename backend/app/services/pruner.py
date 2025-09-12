from ..config import settings
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from .models.data_item import DataItem
from .vector_db import delete_vector

def prune_data(db: Session, dry_run: bool):
    date = datetime.utcnow() - timedelta(days=settings.TTL_DAYS)
    items = db.query(DataItem).filter(DataItem.created_at < date, DataItem.soft_deleted == False).all()
    candidates = [item.id for item in items]
    if not dry_run:
        for item in items:
            item.soft_deleted = True
            delete_vector(item.id)
        db.commit()
    return candidates