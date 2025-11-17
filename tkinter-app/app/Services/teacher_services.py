from app.models.teacher import Teacher

teachers = []

def add_teacher(name, subject):
    t = Teacher(name, subject)
    teachers.append(t)
    return t

def list_teachers():
    return teachers

def update_teacher(index, name, subject):
    if 0 <= index < len(teachers):
        teachers[index].name = name
        teachers[index].subject = subject
        return True
    return False

def delete_teacher(index):
    if 0 <= index < len(teachers):
        teachers.pop(index)
        return True
    return False
