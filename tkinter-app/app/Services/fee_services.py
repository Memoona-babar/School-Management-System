from app.models.fee import Fee

fees = []

def add_fee(student_name, amount, paid):
    f = Fee(student_name, amount, paid)
    fees.append(f)
    return f

def list_fees():
    return fees
