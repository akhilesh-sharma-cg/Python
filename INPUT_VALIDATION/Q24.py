balance = 10000

amount = int(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance or amount % 100 != 0:
    print("Invalid amount. Please try again.")
    amount = int(input("Enter withdrawal amount: "))

balance = balance - amount

print("Withdrawn amount: ₹", amount)
print("Remaining balance: ₹", balance)