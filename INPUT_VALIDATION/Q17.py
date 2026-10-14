balance = 10000

choice = 0

while choice != 4:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current balance: ₹", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        while amount <= 0:
            print("Deposit must be greater than zero.")
            amount = float(input("Enter deposit amount: "))

        balance = balance + amount
        print("Deposit successful.")
        print("Current balance: ₹", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        while amount <= 0 or amount > balance:
            print("Invalid amount. Enter an amount greater than zero and not exceeding your balance.")
            amount = float(input("Enter withdrawal amount: "))

        balance = balance - amount
        print("Withdrawal successful.")
        print("Current balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using our banking program.")

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        choice = 0