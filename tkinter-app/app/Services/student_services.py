from app.models.student import Student
from app.services.student_service import add_student, list_students, update_student, delete_student

students = []

def add_student(name, class_name):
    s = Student(name, class_name)
    students.append(s)
    return s

def list_students():
    return students

def update_student(index, name, class_name):
    if 0 <= index < len(students):
        students[index].name = name
        students[index].class_name = class_name
        return True
    return False

def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)
        return True
    return False
