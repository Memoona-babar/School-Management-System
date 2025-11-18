import tkinter as tk
from tkinter import messagebox
from app.services.teacher_service import add_teacher, list_teachers, update_teacher, delete_teacher

class TeacherWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Teacher Management")
        self.geometry("500x400")

        tk.Label(self, text="Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Subject:").pack()
        self.subject_entry = tk.Entry(self)
        self.subject_entry.pack()

        tk.Button(self, text="Add Teacher", command=self.add_teacher).pack(pady=5)
        tk.Button(self, text="Update Selected", command=self.update_teacher).pack(pady=5)
        tk.Button(self, text="Delete Selected", command=self.delete_teacher).pack(pady=5)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack(pady=10)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for idx, t in enumerate(list_teachers()):
            self.listbox.insert(tk.END, f"{idx+1}. {t.name} - {t.subject}")

    def add_teacher(self):
        name = self.name_entry.get()
        subject = self.subject_entry.get()
        if name == "" or subject == "":
            messagebox.showerror("Error", "Enter both Name and Subject")
            return
        add_teacher(name, subject)
        self.refresh_list()

    def update_teacher(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a teacher")
            return
        index = selected[0]
        name = self.name_entry.get()
        subject = self.subject_entry.get()
        if name == "" or subject == "":
            messagebox.showerror("Error", "Enter both Name and Subject")
            return
        update_teacher(index, name, subject)
        self.refresh_list()

    def delete_teacher(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select a teacher")
            return
        index = selected[0]
        delete_teacher(index)
        self.refresh_list()
