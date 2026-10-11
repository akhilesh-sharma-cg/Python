print("1. Programming")
print("2. Mathematics")
print("3. Communication")

choice = int(input("Select category: "))

match choice:
    case 1:
        print("1. Python")
        print("2. Java")
        print("3. C++")

        subject = int(input("Select subject: "))

        match subject:
            case 1:
                print("You selected Python")
            case 2:
                print("You selected Java")
            case 3:
                print("You selected C++")
            case _:
                print("Invalid subject choice")

    case 2:
        print("1. Algebra")
        print("2. Calculus")
        print("3. Statistics")

        subject = int(input("Select subject: "))

        match subject:
            case 1:
                print("You selected Algebra")
            case 2:
                print("You selected Calculus")
            case 3:
                print("You selected Statistics")
            case _:
                print("Invalid subject choice")

    case 3:
        print("1. English")
        print("2. Presentation")
        print("3. Interview Skills")

        subject = int(input("Select subject: "))

        match subject:
            case 1:
                print("You selected English")
            case 2:
                print("You selected Presentation")
            case 3:
                print("You selected Interview Skills")
            case _:
                print("Invalid subject choice")

    case _:
        print("Invalid category choice")