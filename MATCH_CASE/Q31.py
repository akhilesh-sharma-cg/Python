print("1. Personal Banking")
print("2. Business Banking")

banking = int(input("Enter banking type: "))

match banking:
    case 1:
        print("1. Balance")
        print("2. Transfer")
        print("3. Loan")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Balance Selected")
            case 2:
                print("Transfer Selected")
            case 3:
                print("Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1. Balance")
        print("2. Payroll")
        print("3. Business Loan")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")