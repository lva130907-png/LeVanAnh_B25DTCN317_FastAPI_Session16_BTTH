from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import *
from models import *
from schemas import *
from UserService import *

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get('/students/{student_id}', response_model=StudentResponse, status_code=status.HTTP_200_OK)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = get_detail_student(student_id, db)
    if student == 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='k tim thay id'
        )
    
    return student


@app.post("/enrollments", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def dky_sv(data: EnrollmentCreate, db: Session = Depends(get_db)):
    check = register_student(data, db)
    if check == 'student_not_found':
        raise HTTPException(
            status_code=404,
            detail='k tim thay hco sinh'
        )
    
    if check == 'status not is ACTIVE':
        raise HTTPException(status_code=400, detail='status must is active')
    if check == 'course not found':
        raise HTTPException(status_code=404, detail='k tim thay khoa hoc')
    if check == 'status not open':
        raise HTTPException(status_code=400, detail='status must is open')
    if check == 'duplicate register':
        raise HTTPException(status_code=409, detail='hoc vien da dky khoa hoc')
    return check