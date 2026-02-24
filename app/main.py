from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db, engine, Base
from app.models import user 
from app.models import hospital
from app.models import service
from app.models import appointment 
from app.api import auth 
from app.api import hospitals
from app.api import services
from app.api import make_booking
from app.api import doctors 
from jose import jwt
from app.core.security import SECRET_KEY, ALGORITHM


Base.metadata.create_all(bind=engine) 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(hospitals.router, prefix="/hospitals", tags=["Hospitals"])
app.include_router(services.router, prefix="/services", tags=["Services"])
app.include_router(make_booking.router,prefix="/appointments",tags =["Appointments"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])


@app.get("/")
def read_root():
    return {"status": "active"}

@app.get("/test-db")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT PostGIS_Version();"))
        version = result.scalar()
        return {"status": "success", "postgis_version": version}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.get("/users/me", tags=["Users"])
def get_logged_in_user(request: Request, db: Session = Depends(get_db)):
    
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Not logged in")
        
    token = auth_header.replace("Bearer ", "")
    
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
        
    
    db_user = db.query(user.User).filter(user.User.email == user_email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
        
    
    user_name = getattr(db_user, "full_name", getattr(db_user, "name", "User"))
    
    
    return {
        "email": db_user.email,
        "full_name": user_name
    }