from sqlalchemy.orm import Session
from app.models import Vehicle
from app.schemas import VehicleCreate, VehicleUpdate

class InventoryService:
    def __init__(self, db: Session):
        self.db = db

    def get_vehicles(self, skip: int = 0, limit: int = 100):
        return self.db.query(Vehicle).offset(skip).limit(limit).all()

    def create_vehicle(self, vehicle: VehicleCreate):
        db_vehicle = Vehicle(**vehicle.dict())
        self.db.add(db_vehicle)
        self.db.commit()
        self.db.refresh(db_vehicle)
        return db_vehicle

    def update_vehicle(self, vin: str, vehicle: VehicleUpdate):
        db_vehicle = self.db.query(Vehicle).filter(Vehicle.vin == vin).first()
        for key, value in vehicle.dict(exclude_unset=True).items():
            setattr(db_vehicle, key, value)
        self.db.commit()
        self.db.refresh(db_vehicle)
        return db_vehicle 