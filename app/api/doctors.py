
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.doctor import Doctor
from app.models.hospital import Hospital


from app.schemas.doctor_schema import DoctorResponse 

router = APIRouter()


@router.get("/", response_model=List[DoctorResponse]) 
def get_doctors(db: Session = Depends(get_db)):
    
    doctors = db.query(Doctor, Hospital.name.label("hospital_name"))\
                .join(Hospital, Doctor.hospital_id == Hospital.id)\
                .all()
    
    
    results = []
    for doc, hospital_name in doctors:
        results.append({
            "id": doc.id,
            "hospital_id": doc.hospital_id, 
            "first_name": doc.first_name,
            "last_name": doc.last_name,
            "specialty": doc.specialty,
            "bio": doc.bio,                 
            "hospital_name": hospital_name
        })
        
    return results