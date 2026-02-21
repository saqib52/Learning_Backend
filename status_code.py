from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

# '''Status Codes (Professional Communication)
# Right now everything returns 200 OK.That’s not correct.

# | Action         | Correct Status |
# | -------------- | -------------- |
# | GET success    | 200            |
# | POST create    | 201            |
# | DELETE success | 204            |
# | Bad input      | 400            |
# | Unauthorized   | 401            |
# | Not found      | 404            |
# '''
# # Setting Status Code in FastAPI

# Why This Matters
# Frontend developers rely on status codes.
# Example:
# If 201 → show “Account created”
# If 400 → show error
# If 401 → redirect to login
# Backend must communicate clearly.




app= FastAPI()

class CreateUser(BaseModel):
    name: str 
    age: int
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    name: str
    email: EmailStr
    age: int

@app.post("/user", status_code= status.HTTP_201_CREATED)
def create_user(user: CreateUser):
    return user

@app.get("/users/{user_id}", response_model= UserResponse )
def create_user(user: CreateUser, user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=404, detail="User not found")
    else: 
        return {
        "user": user,
        "user_id": user_id 
    }
