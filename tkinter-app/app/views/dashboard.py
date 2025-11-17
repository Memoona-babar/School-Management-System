import tkinter as tk
from app.views.student_form import StudentWindow
from app.views.teacher_form import TeacherWindow
from app.views.attendance_form import AttendanceWindow
from app.views.fee_form import FeeWindow

class DashboardWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("400x400")

        # Welcome label
        tk.Label(self, text="Welcome to School Management System", font=("Arial", 14)).pack(pady=20)

        # Student button
        tk.Button(self, text="Manage Students", width=25, command=lambda: StudentWindow()).pack(pady=5)

        # Teacher button
        tk.Button(self, text="Manage Teachers", width=25, command=lambda: TeacherWindow()).pack(pady=5)

        # Attendance button
        tk.Button(self, text="Manage Attendance", width=25, command=lambda: AttendanceWindow()).pack(pady=5)

        # Fee button
        tk.Button(self, text="Manage Fees", width=25, command=lambda: FeeWindow()).pack(pady=5)
