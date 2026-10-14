quantity = int(input("Enter product quantity: "))

while quantity <= 0:
    print("Quantity must be a positive integer.")
    quantity = int(input("Enter product quantity: "))

price = float(input("Enter unit price: "))

while price <= 0:
    print("Unit price must be greater than zero.")
    price = float(input("Enter unit price: "))

total = quantity * price

print("Total cost:", total)