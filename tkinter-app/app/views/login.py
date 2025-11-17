import tkinter as tk
from tkinter import messagebox

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")
        tk.Label(self,text="Username:").pack(pady=20)
        self.username = tk.Entry(self)
        self.username.pack()

        tk.Label(self, text="Password").pack(pady=5)
        self.password = tk.Entry(self, show="*")
        self.password.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=10)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()

        if user == "" or pwd == "":
            messagebox.showerror("Error", "Enter username & password")
        else:
            messagebox.showinfo("Success", "Login Successful!")