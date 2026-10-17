def bill(item, quantity=1, price=100):
    return quantity * price

print(bill("Pen"))
print(bill("Book", 2, 50))
print(bill("Bag", price=500, quantity=3))