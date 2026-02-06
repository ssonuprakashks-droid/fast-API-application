from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()
class student(BaseModel):
    name: str
    email:str
    age: int
    roll_number:str 
    department:str
class studentResponse(BaseModel):
    id:int
    name:str
    email:str
    age: int
    roll_number:str 
    department:str
   

   
@app.get("/")
def read_root():
    return {"Hello": "World"}


def create_student(student: student):
    return student
def read_student(id: int):
    return studentResponse(id=id, **student.dict())  
def update_student(student_id: int, student: student):
    return studentResponse(id=student_id, **student.dict())   
def delete_student(student_id: int):
    return studentResponse(id=student_id, **student.dict())        
@app.post("/student")
def create_student(student: student):
    return create_student(student)
@app.get("/student/{id}")
def read_student(id: int):
    return read_student(id)
@app.put("/student/{student_id}")
def update_student(student_id: int, student: student):
    return update_student(student_id, student)
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    return delete_student(student_id)    

