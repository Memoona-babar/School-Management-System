import tkinter as tk
from tkinter import messagebox
from app.services.fee_service import add_fee, list_fees

class FeeWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Fee Management")
        self.geometry("500x400")

        # Student Name
        tk.Label(self, text="Student Name:").pack(pady=(10,0))
        self.student_entry = tk.Entry(self)
        self.student_entry.pack()

        # Amount
        tk.Label(self, text="Amount:").pack(pady=(10,0))
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        # Paid (Yes/No)
        tk.Label(self, text="Paid (Yes/No):").pack(pady=(10,0))
        self.paid_entry = tk.Entry(self)
        self.paid_entry.pack()

        # Button
        tk.Button(self, text="Add Fee", width=20, command=self.add_fee).pack(pady=10)

        # Listbox
        self.listbox = tk.Listbox(self, width=60)
        self.listbox.pack(pady=10)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for idx, f in enumerate(list_fees()):
            status = "Paid" if f.paid.lower() in ["yes", "true"] else "Not Paid"
            self.listbox.insert(tk.END, f"{idx+1}. {f.student_name} - {f.amount} - {status}")

    def add_fee(self):
        student_name = self.student_entry.get()
        amount = self.amount_entry.get()
        paid = self.paid_entry.get()
        if student_name == "" or amount == "" or paid == "":
            messagebox.showerror("Error", "Enter all fields")
            return
        add_fee(student_name, amount, paid)
        self.refresh_list()
        self.student_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.paid_entry.delete(0, tk.END)


