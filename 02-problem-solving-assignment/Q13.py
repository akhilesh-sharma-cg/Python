total = 0

for i in range(1, 7):
    unit = int(input("ENTER YOUR UNITS: "))
    bill = 0

    if unit <= 100:
        bill += unit * 5

    elif unit <= 200:
        bill += 100 * 5
        bill += (unit - 100) * 7

    elif unit <= 400:
        bill += 100 * 5
        bill += 100 * 7
        bill += (unit - 200) * 10

    else:
        bill += 100 * 5
        bill += 100 * 7
        bill += 200 * 10
        bill += (unit - 400) * 15

    print("Bill:", bill)

    if bill < 1000:
        print("Low")
    elif bill <= 3000:
        print("Medium")
    else:
        print("High")

    total += bill

print("Total Revenue:", total) 
