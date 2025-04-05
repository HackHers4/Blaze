from pydantic import BaseModel, EmailStr
from typing import List

class Applicant(BaseModel):
    name: str
    email: EmailStr
    skills: List[str]
    experience: int  # in years
    resume_text: str  # ✅ Added for smart matching