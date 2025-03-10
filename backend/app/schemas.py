from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehicleBase(BaseModel):
    make: str
    model: str
    year: int
    price: float
    status: str
    location_id: int

class VehicleCreate(VehicleBase):
    vin: str

class VehicleUpdate(VehicleBase):
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    price: Optional[float] = None
    status: Optional[str] = None
    location_id: Optional[int] = None

class VehicleResponse(VehicleBase):
    vin: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 