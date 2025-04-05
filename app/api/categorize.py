from app.database.db import applicants_collection, jobs_collection
from fastapi import APIRouter, HTTPException
from app.models.categorize_model import CategorizationRequest
from bson import ObjectId
from typing import Dict, List

router = APIRouter()

def calculate_match_score(applicant: Dict, job: Dict) -> Dict:
    """Core matching logic"""
    applicant_skills = set(applicant.get("skills", []))
    job_skills = set(job.get("required_skills", []))
    
    # Skill matching breakdown
    matched_skills = list(applicant_skills & job_skills)
    missing_skills = list(job_skills - applicant_skills)
    
    # Experience comparison
    applicant_exp = applicant.get("experience", 0)
    required_exp = job.get("min_experience", 0)
    experience_match = applicant_exp >= required_exp
    
    # Percentage calculation
    match_percentage = 0
    if job_skills:
        base_percentage = len(matched_skills) / len(job_skills) * 70  # 70% weight for skills
        experience_bonus = 30 if experience_match else 0  # 30% weight for experience
        match_percentage = min(100, int(base_percentage + experience_bonus))
    
    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_match_count": len(matched_skills),
        "total_required_skills": len(job_skills),
        "applicant_experience": applicant_exp,
        "required_experience": required_exp,
        "experience_match": experience_match,
        "match_percentage": match_percentage,
        "fit_category": (
            "Good Fit" if match_percentage >= 75 
            else "Maybe Fit" if match_percentage >= 40 
            else "Bad Fit"
        )
    }

@router.post("/categorize")
def categorize_applicant(data: CategorizationRequest):
    applicant = applicants_collection.find_one({"_id": ObjectId(data.applicant_id)})
    job = jobs_collection.find_one({"_id": ObjectId(data.job_id)})
    
    if not applicant or not job:
        raise HTTPException(status_code=404, detail="Applicant or Job not found")
    
    return calculate_match_score(applicant, job)