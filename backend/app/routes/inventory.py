from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models import Vehicle
from app.schemas import VehicleCreate, VehicleUpdate, VehicleResponse
from app.database import get_db
from app.services.inventory import InventoryService

router = APIRouter()

@router.get("/vehicles")
def get_vehicles(db: Session = Depends(get_db)):
    return InventoryService(db).get_vehicles()

@router.post("/vehicles/", response_model=VehicleResponse)
def create_vehicle(
    vehicle: VehicleCreate,
    db: Session = Depends(get_db)
):
    return InventoryService(db).create_vehicle(vehicle)

@router.put("/vehicles/{vin}", response_model=VehicleResponse)
def update_vehicle(
    vin: str,
    vehicle: VehicleUpdate,
    db: Session = Depends(get_db)
):
    return InventoryService(db).update_vehicle(vin, vehicle) 