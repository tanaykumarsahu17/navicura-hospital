from sqlalchemy import Column, Integer, String, Float
from geoalchemy2 import Geometry  
from app.core.database import Base
from sqlalchemy.orm import relationship

class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, index=True)
    
    
    
    location = Column(Geometry(geometry_type='POINT', srid=4326)) 
    
    rating = Column(Float, default=0.0)
    image_url = Column(String, nullable=True)

    services = relationship("Service", back_populates="hospital")
    
    appointments = relationship("Appointment", back_populates="hospital")