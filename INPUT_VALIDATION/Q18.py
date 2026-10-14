month = int(input("Enter month number (1-12): "))

while month < 1 or month > 12:
    print("Invalid month. Try again.")
    month = int(input("Enter month number (1-12): "))

day = int(input("Enter day number (1-31): "))

while day < 1 or day > 31:
    print("Invalid day. Try again.")
    day = int(input("Enter day number (1-31): "))

print("Month and day are valid.")