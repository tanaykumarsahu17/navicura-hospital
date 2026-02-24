from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.models.hospital import Hospital
from geoalchemy2.elements import WKTElement
from geoalchemy2.shape import to_shape

router = APIRouter()

@router.post("/seed")
def seed_hospitals(db: Session = Depends(get_db)):
    
    dummy_data = [
        {"name": "City General Hospital", "lat": 12.9716, "long": 77.5946, "address": "M.G Road"},
        {"name": "Sunrise Health Clinic", "lat": 12.9780, "long": 77.6000, "address": "Cubbon Park"},
        {"name": "Westside Trauma Center", "lat": 12.9600, "long": 77.5800, "address": "Lalbagh West"},
        {"name": "Far Away Medical", "lat": 13.1000, "long": 77.5900, "address": "North Hills"},
    ]

    for item in dummy_data:
        point = WKTElement(f'POINT({item["long"]} {item["lat"]})', srid=4326)
        hospital = Hospital(
            name=item["name"],
            address=item["address"],
            city="Bangalore",
            location=point,
            rating=4.5
        )
        db.add(hospital)

    db.commit()
    return {"status": "success", "message": "Added 4 dummy hospitals!"}

@router.get("/near-me")
def get_nearby_hospitals(lat: float, long: float, radius_km: float = 5.0, db: Session = Depends(get_db)):
    user_location = WKTElement(f'POINT({long} {lat})', srid=4326)

    
    distance_calc = func.ST_DistanceSphere(Hospital.location, user_location).label("distance")
    
    
    results_query = db.query(Hospital, distance_calc).filter(
        func.ST_DWithin(Hospital.location, user_location, radius_km * 1000)
    ).all()

    results = []
    
    for hospital, distance_meters in results_query:
        point = to_shape(hospital.location)
        
        results.append({
            "id": hospital.id,
            "name": hospital.name,
            "address": hospital.address,
            "city": hospital.city,
            "rating": hospital.rating,
            "latitude": point.y,
            "longitude": point.x,
            "distance_km": round(distance_meters / 1000, 2) 
        })

    return results