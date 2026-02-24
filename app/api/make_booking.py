import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.appointment import Appointment
from app.models.service import Service
from app.schemas.appointment_schema import AppointmentCreate
from app.schemas.appointment_schema import AppointmentOut
from app.api.deps import get_current_user
from app.models.user import User
from typing import List

router = APIRouter()

@router.post("/book")
def book_appointment(
    booking: AppointmentCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    service = db.query(Service).filter(Service.id == booking.service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    
    new_appointment = Appointment(
        user_id=current_user.id,
        service_id=booking.service_id,
        hospital_id=booking.hospital_id,
        appointment_time=booking.appointment_time,
        status="Pending"
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return {"status": "success", "appointment_id": new_appointment.id, "message": "Booking Confirmed!"}

@router.get("/me", response_model=List[AppointmentOut])
def get_my_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) 
):
    
    
    appointments = db.query(Appointment).filter(Appointment.user_id == current_user.id).all()
    
    return appointments

@router.post("/pay/{appointment_id}")
def pay_for_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    appointment = db.query(Appointment).filter(
        Appointment.id == appointment_id,
        Appointment.user_id == current_user.id
    ).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    if appointment.status == "Confirmed":
         raise HTTPException(status_code=400, detail="Already paid!")

    
    
    fake_transaction_id = f"TXN_{uuid.uuid4().hex[:10].upper()}"

    
    appointment.status = "Confirmed"
    
    
    
    db.commit()
    
    return {
        "status": "success", 
        "message": "Payment Successful", 
        "new_status": appointment.status,
        "transaction_id": fake_transaction_id
    }