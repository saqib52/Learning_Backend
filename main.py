# https://chatgpt.com/c/697e5416-e5f8-8321-8c07-f89cff63df4f

# You are importing a class named FastAPI from the fastapi module.
from fastapi import FastAPI

# “I am bringing a blueprint (class) that knows how to build an API server.”
# You are creating an object (instance) of the FastAPI class.

from fastapi.params import Body

app = FastAPI()

# print(help(FastAPI))
# FastAPI.__dict__

# app now holds: Routes, Configuration, Middleware, Docs setup, Request/response handling logic
# A specific path operation



# @app.get("/") and @app.get("/login") tell FastAPI which function to run for which URL path.
# A decorator app is an object .get() is a method that method stores route info inside the app object
# “When the server receives an HTTP GET request at this URL path, run the function written below.”
@app.get("/")
def root():
    return {"Message": "Hello World"}

'''Path Parametrs: we can pass parameters through path with variables in path like user_id and 
then matching name should be define inside route function 
A path parameter is a variable inside the URL.
/users/{user_id} “Whatever value comes here, capture it and give it to my function.”
'''
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"Name":"Saqib Jawad",
            "user_id": user_id}


@app.get("/users/{user_id}/posts/{user_post}")
async def get_user(user_id: int, user_post: str):
    return {
            "Name":"Saqib Jawad", 
            "user_id" : user_id,
            "user_post": user_post}

@app.post("/createuser/{user_id}")
def create_user(user_id:int):
    return {"User Created":"successfully created user", 
            "user_id": user_id}

@app.delete("/deleteuser/{user_id}")
async def delete_user(user_id: int):
    return {"User Deleted":"successfully deleted user"}

@app.put("/updateuser/{user_id}")
async def update_profile(user_id: int):
    return {"User Update":"successfully Updated user profile"}

@app.patch("/updatepart/{user_id}")
async def update_password(user_id: int):
    return {"updatepassword":"successfully updated password"}


from typing import Union
@app.post("/createuser/typed/{user_id}")
def create_user(user_id: Union[int, str]):
    return {
        "User Created": "successfully created user",
        "user_id": user_id,
        "type": str(type(user_id))
    }

# if we want both int and str as path parameters


''' What Problem Do Query Parameters Solve? '''
'''If you want Only 10 items, Sorted, Filtered, Optional settings
You cannot put all that in the path, So we use query parameters.'''
# # Query parameters are extra information sent in the URL after ?.
# They are not part of the path.
# Inside URL path {} → Path parameter
# Function argument with default value → Query parameter

@app.get("/items")
def get_items(limit: int = 10):
    return{"limit": limit}


@app.get("/products")
def get_products(category: str, in_stock: bool = True):
    return {
        "category": category,
        "in_stock": in_stock
    }
'''try''' 
# /products?category=books
# /products?category=books&in_stock=false


# Path + Query Together (Real API Pattern)

@app.get("/users/{user_id}/orders")
def get_orders(user_id: int, limit: int =5):
    return{
        "user_id":user_id,
        "limit": limit
    }

# /products?category=SUVs&price_min=5000000&sort=asc
@app.get("/cars/")
def get_productbyQP(category: str,price_min: int, sort: object):
    return{"product" : "car",
           "category": category,
           "price_min": price_min,
           "arrange" : sort
    }
'''Path = identity
Query = options'''

# optional vs required query parametrs
# Optional Query Parameter kya hota hai?

# Optional ka matlab:
# 👉 Agar bhejo to bhi chale
# 👉 Agar na bhejo to bhi API kaam kare

'''q: str | None = None'''
# Iska matlab:
# q string ho sakta hai
# ya None ho sakta hai
# default value = None
# Is liye FastAPI kehta hai:
# “Agar q aaye to le lo, warna chhor do”


@app.get("/Instagramposts")
async def get_posts(category: str | None = None):
    if category:
        return {"filter": f"Posts of {category}"}
    return {"filter": "All posts"}

# testing
# /Instagramposts
# /Instagramposts?category=travel

@app.get("/search")
def get_page(q: str, page: int= 1):
    return{ "q": q,
           "page" : page}
# Test:
# /search?q=fastapi
# /search?q=fastapi&page=3
# /search (observe error)

@app.post("/login")
def login(email: str, password: str):
    return {"email": email}


'''Lesson 6: POST Requests & Request Body (Sending Data Properly)
We request data through Get by putting data in the URL(Path and Query)
While we send data to backen, data goes in the request body '''