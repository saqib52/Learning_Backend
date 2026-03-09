from fastapi import FastAPI
from sqlmodel import Session, select
from model import connection, Teachers, Admin
app = FastAPI()

@app.get("/getTeachers")
def get_teachers():
    with Session(connection) as session:
        # executing a task
        statement = select(Teachers)
        result = session.exec(statement)
        data = result.all()
        return data 
    
@app.get("/getAdmins")
def get_admin():
    with Session(connection) as session:
        statement = select(Admin)
        result= session.exec(statement)
        data = result.all()
        return data