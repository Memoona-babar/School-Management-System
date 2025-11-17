import pytest
from app.services.student_service import add_student, list_students, update_student, delete_student, students

def setup_function():
    # Clear students before each test
    students.clear()

def test_add_student():
    s = add_student("Ali", "10th")
    assert s.name == "Ali"
    assert s.class_name == "10th"
    assert len(students) == 1

def test_list_students():
    add_student("Ali", "10th")
    add_student("Sara", "9th")
    lst = list_students()
    assert len(lst) == 2
    assert lst[0].name == "Ali"
    assert lst[1].name == "Sara"

def test_update_student():
    add_student("Ali", "10th")
    updated = update_student(0, "AliUpdated", "11th")
    assert updated is True
    assert students[0].name == "AliUpdated"
    assert students[0].class_name == "11th"

def test_update_invalid_index():
    updated = update_student(5, "NoOne", "1st")
    assert updated is False

def test_delete_student():
    add_student("Ali", "10th")
    deleted = delete_student(0)
    assert deleted is True
    assert len(students) == 0

def test_delete_invalid_index():
    deleted = delete_student(3)
    assert deleted is False
