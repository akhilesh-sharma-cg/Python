print("1.Opening Account Balance\n 2.Opening Mini Statement\n3.Opening Fund Transfer\n 4.Opening Bill Payment \n5.Opening Customer Support ")

match service:
    case 1:
        print("Opening Account Balance")
    case 2:
        print("Opening Mini Statement")
    case 3:
        print("Opening Fund Transfer")
    case 4:
        print("Opening Bill Payment")
    case 5:
        print("Opening Customer Support")
    case _:
        print("Invalid service")