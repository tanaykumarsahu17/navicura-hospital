from pydantic import BaseModel
from typing import Optional


class DoctorBase(BaseModel):
    first_name: str
    last_name: str
    specialty: Optional[str] = None
    bio: Optional[str] = None


class DoctorResponse(DoctorBase):
    id: int
    hospital_id: int
    hospital_name: str 

    class Config:
        from_attributes = True