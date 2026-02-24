from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    service_id: int
    hospital_id: int
    appointment_time: datetime  

class AppointmentOut(BaseModel):
    id: int
    service_id: int
    hospital_id: int
    appointment_time: datetime
    status: str
    
    class Config:
        from_attributes = True