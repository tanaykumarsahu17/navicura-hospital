from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.service import Service
from app.models.hospital import Hospital

router = APIRouter()


@router.post("/seed")
def seed_services(db: Session = Depends(get_db)):
    
    hospital = db.query(Hospital).first()
    if not hospital:
        return {"error": "No hospitals found! Run /hospitals/seed first."}

    
    dummy_services = [
        {"name": "General Consultation", "price": 500.0, "description": "Standard checkup with doctor"},
        {"name": "Blood Test (CBC)", "price": 1200.0, "description": "Complete blood count analysis"},
        {"name": "MRI Scan", "price": 4500.0, "description": "Full body imaging"},
        {"name": "X-Ray", "price": 800.0, "description": "Chest or limb X-ray"},
    ]

    
    for item in dummy_services:
        service = Service(
            name=item["name"],
            price=item["price"],
            description=item["description"],
            hospital_id=hospital.id  
        )
        db.add(service)
    
    db.commit()
    return {"status": "success", "message": f"Added 4 services to Hospital: {hospital.name}"}


@router.get("/{hospital_id}")
def get_services_by_hospital(hospital_id: int, db: Session = Depends(get_db)):
    services = db.query(Service).filter(Service.hospital_id == hospital_id).all()
    return services