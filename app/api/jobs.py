from fastapi import APIRouter
from app.models.job_model import Job
from app.database.db import jobs_collection

router = APIRouter()

@router.post("/jobs")
def create_job(job: Job):
    result = jobs_collection.insert_one(job.dict())
    return str(result.inserted_id)
