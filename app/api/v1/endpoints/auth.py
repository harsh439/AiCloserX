from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth import Login, Token
from app.utils.token import create_access_token

router = APIRouter()

# Login API - returns JWT token
@router.post("/login", response_model=Token)
async def login(login: Login):
    # Simulating user validation for demo purposes
    if login.username == "admin" and login.password == "password":
        token = create_access_token(data={"sub": login.username})
        return {"access_token": token, "token_type": "bearer"}
    
    raise HTTPException(status_code=400, detail="Invalid credentials")
