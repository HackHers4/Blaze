from pydantic import BaseModel

class CategorizationRequest(BaseModel):
    applicant_id: str
    job_id: str