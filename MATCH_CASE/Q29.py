print("1. Search Book")
print("2. Issue Book")
print("3. Return Book")
print("4. View Issued Books")
print("5. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Search Book")
    case 2:
        print("Issue Book")
    case 3:
        print("Return Book")
    case 4:
        print("View Issued Books")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")