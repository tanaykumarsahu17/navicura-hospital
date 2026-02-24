from pydantic import BaseModel
from typing import Optional, Any

class HospitalResponse(BaseModel):
    id: int
    name: str
    address: str
    city: str
    rating: float
    
    
    
    class Config:
        from_attributes = True