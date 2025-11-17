import tkinter as tk
from tkinter import messagebox
from .dashboard import DashboardWindow  # relative import since same folder

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School Management - Login")
        self.geometry("400x250")

        # Username
        tk.Label(self, text="Username:").pack(pady=(30,5))
        self.username = tk.Entry(self)
        self.username.pack(pady=5)

        # Password
        tk.Label(self, text="Password:").pack(pady=5)
        self.password = tk.Entry(self, show="*")
        self.password.pack(pady=5)

        # Login Button
        tk.Button(self, text="Login", width=15, command=self.login).pack(pady=20)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()

        if user == "" or pwd == "":
            messagebox.showerror("Error", "Enter username & password")
        else:
            messagebox.showinfo("Success", f"Welcome {user}!")
            self.destroy()  # Close login window
            dashboard = DashboardWindow()  # Open dashboard window
            dashboard.mainloop()
