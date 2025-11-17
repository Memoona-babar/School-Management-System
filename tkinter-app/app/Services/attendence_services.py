from app.models.attendance import Attendance

attendances = []

def add_attendance(student_name, date, status):
    a = Attendance(student_name, date, status)
    attendances.append(a)
    return a

def list_attendance():
    return attendances
