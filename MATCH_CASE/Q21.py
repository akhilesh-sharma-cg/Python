choice = int(input("Enter choice: "))
temperature = float(input("Enter temperature: "))

match choice:
    case 1:
        f = (temperature * 9/5) + 32
        print("Temperature =", f, "F")
    case 2:
        c = (temperature - 32) * 5/9
        print("Temperature =", c, "C")
    case _:
        print("Invalid choice")