import tkinter as tk
from tkinter import messagebox
from app.services.attendance_service import add_attendance, list_attendance
from datetime import datetime

class AttendanceWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Attendance Management")
        self.geometry("500x400")

        # Student Name
        tk.Label(self, text="Student Name:").pack(pady=(10,0))
        self.student_entry = tk.Entry(self)
        self.student_entry.pack()

        # Date
        tk.Label(self, text="Date (YYYY-MM-DD):").pack(pady=(10,0))
        self.date_entry = tk.Entry(self)
        self.date_entry.pack()
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        # Status
        tk.Label(self, text="Status (Present/Absent):").pack(pady=(10,0))
        self.status_entry = tk.Entry(self)
        self.status_entry.pack()

        # Button
        tk.Button(self, text="Add Attendance", width=20, command=self.add_attendance).pack(pady=10)

        # Listbox
        self.listbox = tk.Listbox(self, width=60)
        self.listbox.pack(pady=10)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for idx, a in enumerate(list_attendance()):
            self.listbox.insert(tk.END, f"{idx+1}. {a.student_name} - {a.date} - {a.status}")

    def add_attendance(self):
        student_name = self.student_entry.get()
        date = self.date_entry.get()
        status = self.status_entry.get()
        if student_name == "" or date == "" or status == "":
            messagebox.showerror("Error", "Enter all fields")
            return
        add_attendance(student_name, date, status)
        self.refresh_list()
        self.student_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)
