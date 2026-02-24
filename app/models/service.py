from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)  
    price = Column(Float, nullable=False)              
    description = Column(String, nullable=True)
    
    
    hospital_id = Column(Integer, ForeignKey("hospitals.id"))

    
    hospital = relationship("Hospital", back_populates="services")
    
    appointments = relationship("Appointment", back_populates="service")