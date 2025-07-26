from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/tenants", tags=["Tenants"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TenantOut)
def create_tenant(tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    new_tenant = models.Tenant(**tenant.dict())
    db.add(new_tenant)
    db.commit()
    db.refresh(new_tenant)
    return new_tenant

@router.get("/", response_model=list[schemas.TenantOut])
def get_tenants(db: Session = Depends(get_db)):
    return db.query(models.Tenant).all()
