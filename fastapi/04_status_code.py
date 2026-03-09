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

@app.post("/users", status_code= status.HTTP_201_CREATED, response_model=UserResponse) 
def create_user(user: CreateUser):
    if user.age < 18:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="user must be atleast 18 year old")
    return{"name":user.name,
           "age":user.age,
           "email": user.email
           }



@app.get("/users/{user_id}",response_model= UserResponse )
def create_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "name": "Saqib",
        "age": 30,
        "email": "saqibjawad52@gmail.com"
    }

# # FastAPI:
# # Stops execution
# # Returns proper error JSON
# # Sets correct status code
# This is clean and consistent.