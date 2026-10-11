print("1. Regular")
print("2. Premium")
print("3. VIP")

choice = int(input("Select ticket type: "))

match choice:
    case 1:
        ticket = "Regular"
    case 2:
        ticket = "Premium"
    case 3:
        ticket = "VIP"
    case _:
        ticket = "Invalid choice"

if ticket == "Invalid choice":
    print("Invalid choice")
else:
    age = int(input("Enter your age: "))

    if age < 5:
        print("Free Entry")
    else:
        print(ticket)