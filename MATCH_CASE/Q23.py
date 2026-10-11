account = int(input("Enter account type: "))

match account:
    case 1:
        print("Savings Account")
    case 2:
        print("Current Account")

amount = int(input("Enter amount: "))

if amount >0:
    print("Withdrawal Request Accepted")
else:
    print("Invalid Amount")