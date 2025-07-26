# ✅ auth.py (inside login route)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from jose import jwt, JWTError
from database import get_db
import models, schemas, utils

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/token")
def login(credentials: schemas.LoginInput, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == credentials.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid Email")
    if not utils.verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Password")
    
    token = utils.create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
