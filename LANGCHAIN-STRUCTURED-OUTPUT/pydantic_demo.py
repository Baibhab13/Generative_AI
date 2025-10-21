from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str = 'baibhab'
    age: Optional[int] = None
    email : EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decmial value respresenting the cgpa of the student') # type: ignore


new_student = {'age': '25', 'email': 'abcgmail.com'}

student = Student(**new_student)

print(student)