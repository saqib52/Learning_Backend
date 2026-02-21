# https://chatgpt.com/c/697e5416-e5f8-8321-8c07-f89cff63df4f

# You are importing a class named FastAPI from the fastapi module.
from fastapi import FastAPI

# “I am bringing a blueprint (class) that knows how to build an API server.”
# You are creating an object (instance) of the FastAPI class.
# @app.get("/") and @app.get("/login") tell FastAPI which function to run for which URL path.
# A decorator app is an object .get() is a method that method stores route info inside the app object
# “When the server receives an HTTP GET request at this URL path, run the function written below.”
# print(help(FastAPI))
# FastAPI.__dict__

# app now holds: Routes, Configuration, Middleware, Docs setup, Request/response handling logic
# A specific path operation

from fastapi.params import Body
app = FastAPI()

@app.get("/")
def root():
    return {"Message": "Hello World"}