'''Lesson 6: POST Requests & Request Body (Sending Data Properly)
We request data through Get by putting data in the URL(Path and Query)
While we send data to backen, data goes in the request body '''

'''What is a Request Body?
A request body is the data sent by the client (usually JSON) to the server in 
HTTP methods like:POST,PUT,PATCH'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
 
'''BaseModel kya hoti hai?

👉 BaseModel Pydantic ki main / parent class hoti hai
👉 Jab bhi aap koi Pydantic model banate ho, wo BaseModel se inherit karta hai'''

'''Ye class:
1-Data ka structure define karti hai
2-Data ko validate karti hai
3-JSON ko Python object bana deti hai.
Ye class batati hai: request body mein konsa data aayega, kis type ka hoga, aur valid hai ya nahi'''

'''yaha User ek pydantic model hain
jo vallidation karta hai: Validation = data ko check karna ke wo sahi format aur rules ke mutabiq hai
# Pydantic model ek rule book / blueprint hota hai jo batata hai:
# Data mein kaun se fields hon
# Har field ka data type kya ho
# Data sahi hai ya ghalat (validation)

# basemodel say kya inherit ho ga
# Data Validation,Parsing,Required Fields Check,Automatic Error Messages,Python Object bana deta hai,JSON → Python object'''

class User(BaseModel):
    name: str
    age: int 
    email: str

@app.post("/users/")
def create_user(user: User):
    return{
        "message":"User created",
        'email': user.email,
        "user": user,     
    }

class RegisterAcc(BaseModel):
    username: str
    emails: str
    password: str

@app.post("/register/")
def register_account(user: RegisterAcc):
    return{"message": "user registered",
           "user": user,
           "email": user.emails,
           "name": user.username,
           "password": user.password
           }

'''Lesson no 7: Response Model is a Pydantic model that defines the structure of the data your API returns to the client.
In previous Sections, We have validated the input data, required fields and returned raw dictionaries.
Now we control, what the client is allowed to see, what status code is returned & how professional our API look'''

'''Even if your database returns many fields, you might not want to expose all of them (e.g., passwords).

# A response model helps:
# Control what is sent to users like you send password in previous request (Not Safe)
# Improve security
# Keep API responses consistent
# Generate clean API docs'''

'''soultion to problem'''
# Solution: Separate Input Model & Output Model

#creating input model
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Creating response model  
class UserResponse(BaseModel):
    username: str
    email: str

@app.post("/users", response_model = UserResponse)
def create_users(user: UserCreate):
    return user

# Now FastAPI: Automatically filters output, Removes password

'''Note: Request with GET/HEAD method cannot have body.'''
# Creating response model only 
class UserRes(BaseModel):
    id: int
    username: str
    email: str

@app.get("/userr/{user_id}", response_model = UserRes)
def get_users( user_id:int):
    return {"id": user_id,
        "username": "saqib",
        "email": "saqib@email.com"}

# Example #2:
# Email validation

from typing import Optional
from pydantic import BaseModel, EmailStr

# ----------------------------
# 📥 REQUEST BODY MODEL
# ----------------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    password: str
    bio: Optional[str] = None

# ----------------------------
# 📥 RESPONSE BODY MODEL
# ----------------------------

class UserResponse(BaseModel):
    name: str
    email: EmailStr
    age: int

@app.post("/userx",response_model= UserResponse)
def create_user(user: UserCreate):
    return {"name": user.name,
        "email": user.email,
        "age": user.age,
        'password': user.password
        }