from models import *
from schemas import *
from sqlalchemy.orm import Session


def get_detail_student(student_id: int, db: Session):
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if student is None:
        return 1
    
    lst_course = [
        i.course for i in student.enrollments
    ]
    return {
        'student_id': student.id,
        'full_name': student.full_name,
        'status': student.status,
        'department': student.department,
        'enrollments': lst_course
    }


def register_student(data: EnrollmentCreate, db: Session):
    student = db.query(StudentModel).filter(StudentModel.id == data.student_id).first()
    if student is None:
        return 'student_not_found'
    
    if student.status != 'ACTIVE':
        return 'status not is ACTIVE'
    
    course = db.query(CourseModel).filter(CourseModel.id == data.course_id).first()
    if course is None:
        return 'course not found'
    
    if course.status != 'OPEN':
        return 'status not open'
    
    is_duplicate = db.query(EnrollmentModel).filter(
        EnrollmentModel.course_id == data.course_id,
        EnrollmentModel.student_id == data.student_id
    ).first()

    if is_duplicate is not None:
        return 'duplicate register'
    
    new_enrollment = EnrollmentModel(
        course_id = data.course_id,
        student_id = data.student_id
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return new_enrollment
