from fastapi import FastAPI

# Import SQLModel classes for database operations/DB tools
# Session → to interact with DB
# select → to query data
# create_engine → to connect to the database
from sqlmodel import Session, select, create_engine

# Import your table models (Teachers, Admin) defined in models.py
from models import Teachers, Admin

# os module → to read environment variables
import os

# dotenv → to load variables from .env file
from dotenv import load_dotenv

load_dotenv()  # read DATABASE_URL from .env

app = FastAPI()

# Get the Database connection string from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an engine → this is like opening a connection to the database
# Engine manages the connection pool and communicates with the DB
engine = create_engine(DATABASE_URL)

# Define an API route /getTeachers using the @app.get decorator
# This function will be called when someone visits http://127.0.0.1:8000/getTeachers
@app.get("/getTeachers")
def get_teachers():
    # Open a session to interact with the database
    # Session is like opening a workspace where queries are executed
    with Session(engine) as session:
        statement = select(Teachers) # SELECT * FROM Teachers
        result = session.exec(statement) # Execute the query in the session
         # Fetch all results and return as a list of Teachers
        # FastAPI will automatically convert this into JSON for the client
        return result.all() 
    
