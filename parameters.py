
'''Path Parametrs: we can pass parameters through path with variables in path like user_id and 
then matching name should be define inside route function 
A path parameter is a variable inside the URL.
/users/{user_id} “Whatever value comes here, capture it and give it to my function.”
'''
from fastapi import FastAPI

app = FastAPI()

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
def get_items(limit_is: int = 10):
    return{"limit_is": limit_is}


@app.get("/products")
def get_products(category: str, in_stock: bool = True):
    return {
        "category_is": category,
        "in_stock": in_stock
    }
'''try''' 
# /products?category=books
# /products?category=books&in_stock=false


# Path + Query Together (Real API Pattern)

@app.get("/users/{user_id}/orders")
def get_orders(user_id: int, order_limit: int =5):
    return{
        "user_id":user_id,
        "limit": order_limit
    }

# /products?category=SUVs&price_min=5000000&sort=asc
@app.get("/cars")
def get_productbyQP(category: str, price_min: int, sort: object):
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
def get_posts(category: str | None = None):
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
    return {"email": email,
            'password': password}