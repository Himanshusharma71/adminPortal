from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas, utils

router = APIRouter(prefix="/config", tags=["Source Config"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def save_config(config: schemas.SourceConfigCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash_password(config.password)
    db_config = models.SourceConfig(
        tenant_id=config.tenant_id,
        host=config.host,
        port=config.port,
        username=config.username,
        password=hashed_password
    )
    db.add(db_config)
    db.commit()
    return {"message": "Source config saved"}
