from fastapi import FastAPI
from app.api.applicants import router as applicants_router
from app.api.jobs import router as jobs_router
from app.api.categorize import router as categorize_router

app = FastAPI()

app.include_router(applicants_router, prefix="/applicants")
app.include_router(jobs_router, prefix="/jobs")
app.include_router(categorize_router, prefix="/categorize")

@app.get("/")
def read_root():
    return {"message": "SmartMatch Backend is running"}