import tkinter as tk
from tkinter import messagebox

class DashboardWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.geometry("400x300")

        tk.Label(self, text="Welcome to School Management System", font=("Arial", 14)).pack(pady=20)

        tk.Button(self, text="Manage Students", width=20, command=self.manage_students).pack(pady=5)
        tk.Button(self, text="Manage Teachers", width=20, command=self.manage_teachers).pack(pady=5)

    def manage_students(self):
        messagebox.showinfo("Students", "Student management placeholder")

    def manage_teachers(self):
        messagebox.showinfo("Teachers", "Teacher management placeholder")
