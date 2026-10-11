print("1.ELECTRONICS\n 2.CLOTHING\n3.BOOKS\n 4.GROCERY \n5.EXIT ")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")