from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from datetime import datetime
from typing import List
from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerResponse
from app.db import get_db

router = APIRouter()

# Create a new customer
@router.post("/", response_model=CustomerResponse)
async def create_customer(customer: CustomerCreate, db = Depends(get_db)):
    customer_data = customer.dict()
    customer_data['created_at'] = datetime.utcnow()  # Set created_at timestamp
    result = db["customers"].insert_one(customer_data)
    created_customer = db["customers"].find_one({"_id": result.inserted_id})
    if created_customer is None:
        raise HTTPException(status_code=400, detail="Customer creation failed")
    return created_customer

# Get a customer by ID
@router.get("/{customer_id}", response_model=CustomerResponse)
async def get_customer(customer_id: str, db = Depends(get_db)):
    if not ObjectId.is_valid(customer_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    
    customer = db["customers"].find_one({"_id": ObjectId(customer_id)})
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    return customer

# Update a customer by ID
@router.put("/{customer_id}", response_model=CustomerResponse)
async def update_customer(customer_id: str, customer_update: CustomerUpdate, db = Depends(get_db)):
    if not ObjectId.is_valid(customer_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    
    update_data = {k: v for k, v in customer_update.dict().items() if v is not None}
    
    result = db["customers"].update_one({"_id": ObjectId(customer_id)}, {"$set": update_data})

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Customer not found")

    updated_customer = db["customers"].find_one({"_id": ObjectId(customer_id)})
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found after update")
    
    return updated_customer

# Delete a customer by ID
@router.delete("/{customer_id}", response_model=dict)
async def delete_customer(customer_id: str, db = Depends(get_db)):
    if not ObjectId.is_valid(customer_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")

    result = db["customers"].delete_one({"_id": ObjectId(customer_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    return {"status": "Customer deleted"}

# Get all customers (optional)
@router.get("/", response_model=List[CustomerResponse])
async def get_all_customers(skip: int = 0, limit: int = 10, db = Depends(get_db)):
    customers = db["customers"].find().skip(skip).limit(limit)
    return list(customers)


"""

Here's the latest, complete and updated version of endpoints/customer.py based on your MongoDB and FastAPI setup. I have ensured that the code follows best practices and handles all CRUD operations for the Customer resource, including:

Creating a new customer.
Retrieving a customer by ID.
Updating a customer.
Deleting a customer.
Basic validation for ObjectId.
"""

"""
Explanation:
Create Customer:

Uses CustomerCreate schema to validate input.
Adds a timestamp (created_at) when creating the customer.
Inserts the new customer into the MongoDB collection.
Retrieves the inserted customer for returning.
Get Customer by ID:

Validates the provided customer_id to ensure it's a valid MongoDB ObjectId.
Fetches the customer from the customers collection and raises an error if not found.
Update Customer by ID:

Validates the provided customer_id and ensures that only fields present in the CustomerUpdate schema are updated.
Uses MongoDB's $set operation to update only the provided fields.
Raises an error if no customer is matched for the update.
Delete Customer by ID:

Validates the customer_id.
Deletes the customer from the MongoDB collection and raises an error if no customer is found for deletion.
Get All Customers (optional):

Implements pagination with skip and limit parameters to fetch a limited set of customers from the MongoDB collection.

Improvements:
Error Handling: Each endpoint includes proper error handling using HTTPException.
Efficient Updates: Only updates the fields that are passed in the request (using $set).
ObjectId Validation: Ensures all incoming ObjectId strings are valid MongoDB ObjectIds.
"""
