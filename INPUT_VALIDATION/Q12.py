balance = 2000

amount = float(input("Enter deposit amount: ₹"))

while amount <= 0:
    print("Invalid amount! Enter a positive amount.")
    amount = float(input("Enter deposit amount: ₹"))

balance = balance + amount

print("New balance: ₹", balance)