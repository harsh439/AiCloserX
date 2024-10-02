from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional
from datetime import datetime

# Custom type to handle ObjectId with Pydantic
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None

    class Config:
        json_encoders = {ObjectId: str}  # Ensure ObjectId is encoded as a string
        allow_population_by_field_name = True

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        json_encoders = {ObjectId: str}

class CustomerResponse(CustomerBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")  # Use PyObjectId for MongoDB ObjectId
    created_at: datetime
    is_active: bool = True

    class Config:
        allow_population_by_field_name = True  # Allow _id to be returned as id
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}  # Ensure ObjectId is encoded as a string
