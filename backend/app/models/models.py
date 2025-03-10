from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = "vehicles"
    
    vin = Column(String(17), primary_key=True)
    make = Column(String(50))
    model = Column(String(50))
    year = Column(Integer)
    price = Column(Float)
    status = Column(String(20))
    location_id = Column(Integer, ForeignKey("locations.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(String(17), ForeignKey("vehicles.vin"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    sale_date = Column(DateTime, default=datetime.utcnow)
    sale_price = Column(Float)
    payment_type = Column(String(20))

class Service(Base):
    __tablename__ = "services"
    
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(String(17), ForeignKey("vehicles.vin"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    service_type = Column(String(50))
    scheduled_date = Column(DateTime)
    status = Column(String(20))
    notes = Column(String(500)) 