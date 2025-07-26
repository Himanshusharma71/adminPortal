from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from datetime import datetime
import random

router = APIRouter(prefix="/health", tags=["Health Monitoring"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

statuses = ["green", "yellow", "red"]
errors = ["No error", "Timeout error", "Connection lost"]

@router.get("/", response_model=list[schemas.HealthOut])
def get_health(db: Session = Depends(get_db)):
    tenants = db.query(models.Tenant).all()
    response = []
    for t in tenants:
        snapshot = models.HealthSnapshot(
            tenant_id=t.id,
            last_sync_time=datetime.utcnow(),
            last_error_message=random.choice(errors),
            status=random.choice(statuses)
        )
        db.add(snapshot)
        db.commit()
        db.refresh(snapshot)
        response.append(snapshot)
    return response
