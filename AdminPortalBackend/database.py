from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./test.db"  # or PostgreSQL connection URL

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # only for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ This is the missing part:
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
