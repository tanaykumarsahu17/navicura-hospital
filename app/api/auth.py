from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserResponse
from app.core.security import get_password_hash
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    
    hashed_password = get_password_hash(user.password)

    
    new_user = User(
        email=user.email,
        password=hashed_password,
        full_name=user.full_name,
        phone=user.phone
    )

    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == form_data.username).first()
    
    
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    
    access_token = create_access_token(
        data={"sub": user.email}
    )
    
    
    return {"access_token": access_token, "token_type": "bearer"}