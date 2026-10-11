print("1. General Medicine")
print("2. Cardiology")
print("3. Orthopedics")
print("4. Pediatrics")
print("5. Emergency")

choice = int(input("Enter department: "))

match choice:
    case 1:
        print("General Medicine")
    case 2:
        print("Cardiology")
    case 3:
        print("Orthopedics")
    case 4:
        print("Pediatrics")
    case 5:
        print("Emergency")
    case _:
        print("Invalid Department")