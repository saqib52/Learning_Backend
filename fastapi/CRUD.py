from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, EmailStr, Field

app= FastAPI()

# Setup Fake Database as temporary memory storage.
fake_user_db = {}

# Defining Models

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


# defining endpoint/path/url for create

@app.post("/users", response_model= UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    user_id = len(fake_user_db) + 1

    user_data = {
        "id": user_id,
        "username": user.username,
        "email": user.email
    }

    fake_user_db[user_id] = user_data
    return user_data, 

# @app.get("/users")
# def get_all_users():
#     return list(fake_user_db.values())