import tkinter as tk
from tkinter import messagebox
from app.services.student_service import add_student, list_students, update_student, delete_student

class StudentWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Student Management")
        self.geometry("500x400")

        # Name
        tk.Label(self, text="Name:").pack(pady=(10,0))
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Class
        tk.Label(self, text="Class:").pack(pady=(10,0))
        self.class_entry = tk.Entry(self)
        self.class_entry.pack()

        # Buttons
        tk.Button(self, text="Add Student", width=20, command=self.add_student).pack(pady=5)
        tk.Button(self, text="Update Selected", width=20, command=self.update_student).pack(pady=5)
        tk.Button(self, text="Delete Selected", width=20, command=self.delete_student).pack(pady=5)

        # Listbox
        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack(pady=10)
        self.refresh_list()

    # Refresh list
    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for idx, student in enumerate(list_students()):
            self.listbox.insert(tk.END, f"{idx+1}. {student.name} - {student.class_name}")

    # Add
    def add_student(self):
        name = self.name_entry.get()
        class_name = self.class_entry.get()
        if name == "" or class_name == "":
            messagebox.showerror("Error", "Enter both Name and Class")
            return
        add_student(name, class_name)
        self.refresh_list()
        self.name_entry.delete(0, tk.END)
        self.class_entry.delete(0, tk.END)

    # Update
    def update_student(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a student")
            return
        index = selected[0]
        name = self.name_entry.get()
        class_name = self.class_entry.get()
        if name == "" or class_name == "":
            messagebox.showerror("Error", "Enter both Name and Class")
            return
        update_student(index, name, class_name)
        self.refresh_list()

    # Delete
    def delete_student(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a student")
            return
        index = selected[0]
        delete_student(index)
        self.refresh_list()
