from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TenantCreate(BaseModel):
    name: str
    email: str
    timezone: str

class TenantOut(TenantCreate):
    id: int
    pipeline_status: bool
    class Config:
        orm_mode = True

class SourceConfigCreate(BaseModel):
    tenant_id: int
    host: str
    port: int
    username: str
    password: str

class PipelineToggle(BaseModel):
    tenant_id: int
    pipeline_status: bool

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

# class UserOut(BaseModel):
#     id: int
#     username: str
#     role: str
#     class Config:
#         orm_mode = True

class UserOut(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True  # ✅ Pydantic v2 style
    }


class Token(BaseModel):
    access_token: str
    token_type: str

class LoginInput(BaseModel):
    username: str
    password: str

class HealthOut(BaseModel):
    tenant_id: int
    last_sync_time: datetime
    last_error_message: str
    status: str

class LoginInput(BaseModel):
    email: str
    password: str

class Config:
    from_attributes = True
