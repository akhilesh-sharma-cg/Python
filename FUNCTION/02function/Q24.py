def apply_discount(price, discount=0):
    final_price = price - (price * discount / 100)
    return final_price

print(apply_discount(1000))
print(apply_discount(1000, 20))