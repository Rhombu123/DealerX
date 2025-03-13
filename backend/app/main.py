from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, inventory, sales, service, employees, customers

app = FastAPI(title="Dealership Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["Inventory"])
app.include_router(sales.router, prefix="/api/sales", tags=["Sales"])
app.include_router(service.router, prefix="/api/service", tags=["Service"])
app.include_router(employees.router, prefix="/api/employees", tags=["Employees"])
app.include_router(customers.router, prefix="/api/customers", tags=["Customers"]) 