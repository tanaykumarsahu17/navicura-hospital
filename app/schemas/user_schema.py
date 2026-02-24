from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    phone: str = None  


class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    
    
    class Config:
        from_attributes = True