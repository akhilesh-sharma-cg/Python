print("1. Book Ticket")
print("2. Cancel Ticket")
print("3. Check PNR")
print("4. Train Schedule")
print("5. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Book Ticket")
    case 2:
        print("Cancel Ticket")
    case 3:
        print("Check PNR")
    case 4:
        print("Train Schedule")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")