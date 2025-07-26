from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    timezone = Column(String)
    pipeline_status = Column(Boolean, default=False)

    source_config = relationship("SourceConfig", back_populates="tenant", uselist=False)

class SourceConfig(Base):
    __tablename__ = "source_configs"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    host = Column(String)
    port = Column(Integer)
    username = Column(String)
    password = Column(String)  # Store hashed

    tenant = relationship("Tenant", back_populates="source_config")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)  # Admin or Viewer

class HealthSnapshot(Base):
    __tablename__ = "health_snapshots"
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    last_sync_time = Column(DateTime)
    last_error_message = Column(String)
    status = Column(String)  # green, yellow, red
