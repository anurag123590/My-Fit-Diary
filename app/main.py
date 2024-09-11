from fastapi import FastAPI
from app.routers import router
from app.database import Base, engine
from .scheduler import scheduler
from fastapi.staticfiles import StaticFiles

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Serve static files
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)