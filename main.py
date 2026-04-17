from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import engine
from models import Base
from database import SessionLocal
from models import StudentDB

Base.metadata.create_all(bind=engine)
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Student(BaseModel):
    name:str
    marks:int

@app.get("/")
def home():
    return{"message":"Student Performance Analyzer API is running"}
@app.post("/students")
def add_student(student:Student):
    db=SessionLocal()
    marks=student.marks
    if marks>=90:
        grade="A"
    elif marks>=75:
        grade="B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    new_student=StudentDB(
        name=student.name,
        marks=marks,
        grade=grade
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return{
        "message":"student added sucessfully",
        "id":new_student.id,
        "name":new_student.name,
        "marks":new_student.marks,
        "grade":new_student.grade
    }
@app.get("/students")
def get_student():
    db=SessionLocal()
    students=db.query(StudentDB).all()
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    db = SessionLocal()

    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()

    if not student:
        return {"message": "student not found"}

    marks = updated_student.marks

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # ✅ MUST be outside conditions
    student.name = updated_student.name
    student.marks = marks
    student.grade = grade

    db.commit()
    db.refresh(student)

    return {
        "message": "Student updated successfully",
        "data": {
            "id": student.id,
            "name": student.name,
            "marks": student.marks,
            "grade": student.grade
        }
    }
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    db = SessionLocal()

    student = db.query(StudentDB).filter(StudentDB.id == student_id).first()

    if not student:
        return {"message": "Student not found"}

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }