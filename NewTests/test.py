transactions = [
    {"type": "income", "amount": 100},
    {"type": "expense", "amount": 40},
    {"type": "income", "amount": 60},
    {"type": "expense", "amount": 10},
]

total_income = 0
total_expense = 0

for d in transactions:
    if d["type"] == "income":
        total_income += d["amount"]
    else:
        total_expense += d["amount"]


result = {
    "income": total_income,
    "expense": total_expense,
    "balance": total_income - total_expense 
}


print(result)