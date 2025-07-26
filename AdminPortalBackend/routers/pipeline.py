from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/pipeline", tags=["Pipeline"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/toggle")
def toggle_pipeline(pipeline: schemas.PipelineToggle, db: Session = Depends(get_db)):
    tenant = db.query(models.Tenant).filter(models.Tenant.id == pipeline.tenant_id).first()
    if not tenant:
        return {"error": "Tenant not found"}
    tenant.pipeline_status = pipeline.pipeline_status
    db.commit()
    return {"status": "updated", "pipeline_status": tenant.pipeline_status}
