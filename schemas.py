from pydantic import BaseModel


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class DepartmentCreate(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

class CourseResponse(BaseModel):
    id: int
    name: str
    status: str
    class Config:
        from_attributes = True


class StudentResponse(BaseModel):
    student_id: int
    full_name: str
    status: str
    department: DepartmentCreate
    enrollments: list[CourseResponse]
    class Config:
        from_attributes = True

class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    class Config:
        from_attributes = True

