from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select
app = FastAPI()
connection_string = 'postgresql://postgres.oeslrhuhisuaxqyspcat:33101-8Pu**@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres'

# “Hello database, mujhe tumse baat karni hai.”
connection = create_engine(connection_string)

# class will create table with following coulmns 
class Teachers(SQLModel, table = True):
    id: int = Field(default = None, primary_key = True)
    Name: str
    age: int
    isactive: bool

class Admin(SQLModel, table = True):
    id: int = Field(default = None, primary_key = True)
    Name: str
    age: int
    isactive: bool

# this will create all table created with sqlmodels    
SQLModel.metadata.create_all(connection)

# @app.get("/getTeachers")
# def get_teachers():
#     with Session(connection) as session:
#         # executing a task
#         statement = select(Teachers)
#         result = session.exec(statement)
#         data = result.all()
#         return data 


# """Aap SQLModel aur SQLAlchemy use kar rahe ho jo PostgreSQL se connect hone ke liye 
# psycopg2 driver use karta hai"""

# Library me jab tak tum kaam kar rahe ho us time ko session samjho.
# Programming me session ek workspace hota hai jahan:
# data read hota hai
# data insert hota hai
# data update hota hai
# data delete hota hai
# Jab kaam khatam ho jata hai to session close ho jata hai.

# """App ka flow normally aisa hota hai:
# App database se connection banata hai
# App ek session open karta hai
# Session me queries chalti hain
# Session close ho jata hai."""