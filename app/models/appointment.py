from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    service_id = Column(Integer, ForeignKey("services.id", ondelete="CASCADE"))
    hospital_id = Column(Integer, ForeignKey("hospitals.id", ondelete="CASCADE"))
    
    appointment_time = Column(DateTime, nullable=False)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    
    user = relationship("User", back_populates="appointments")
    service = relationship("Service", back_populates="appointments")
    hospital = relationship("Hospital", back_populates="appointments")