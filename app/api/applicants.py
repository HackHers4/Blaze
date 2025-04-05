from fastapi import APIRouter
from app.models.applicant_model import Applicant
from app.database.db import applicants_collection
from bson import ObjectId

router = APIRouter()

@router.post("/applicants")
def create_applicant(applicant: Applicant):
    result = applicants_collection.insert_one(applicant.dict())
    return str(result.inserted_id)
