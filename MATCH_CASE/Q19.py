category = int(input("1. Vegetarian\n2. Non-Vegetarian\nEnter category: "))

match category:
    case 1:
        food = int(input("1. Paneer\n2. Dal\n3. Veg Biryani\nEnter food: "))
        match food:
            case 1:
                print("Paneer")
            case 2:
                print("Dal")
            case 3:
                print("Veg Biryani")

    case 2:
        food = int(input("1. Chicken Biryani\n2. Chicken Curry\n3. Fish Fry\nEnter food: "))
        match food:
            case 1:
                print("Chicken Biryani")
            case 2:
                print("Chicken Curry")
            case 3:
                print("Fish Fry")