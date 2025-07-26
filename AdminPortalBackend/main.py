from fastapi import FastAPI
from routers import tenant, source_config, pipeline, user, health, auth_router
from database import Base, engine
import models
from routers import auth


# Create tables in DB
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Multi-Tenant Admin Portal")

# Register all routers
app.include_router(tenant.router)
app.include_router(source_config.router)
app.include_router(pipeline.router)
app.include_router(user.router)
app.include_router(health.router)
app.include_router(auth_router.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Admin Portal Backend is running"}
