print("1. Starters")
print("2. Main Course")
print("3. Desserts")
print("4. Drinks")

category = int(input("Select a category: "))

match category:
    case 1:
        print("1. Soup")
        print("2. Spring Roll")
        print("3. Garlic Bread")

        item = int(input("Select an item: "))

        match item:
            case 1:
                print("Soup Ordered")
            case 2:
                print("Spring Roll Ordered")
            case 3:
                print("Garlic Bread Ordered")
            case _:
                print("Invalid Item")

    case 2:
        print("1. Pizza")
        print("2. Pasta")
        print("3. Biryani")

        item = int(input("Select an item: "))

        match item:
            case 1:
                print("Pizza Ordered")
            case 2:
                print("Pasta Ordered")
            case 3:
                print("Biryani Ordered")
            case _:
                print("Invalid Item")

    case 3:
        print("1. Ice Cream")
        print("2. Cake")
        print("3. Gulab Jamun")

        item = int(input("Select an item: "))

        match item:
            case 1:
                print("Ice Cream Ordered")
            case 2:
                print("Cake Ordered")
            case 3:
                print("Gulab Jamun Ordered")
            case _:
                print("Invalid Item")

    case 4:
        print("1. Coffee")
        print("2. Tea")
        print("3. Juice")

        item = int(input("Select an item: "))

        match item:
            case 1:
                print("Coffee Ordered")
            case 2:
                print("Tea Ordered")
            case 3:
                print("Juice Ordered")
            case _:
                print("Invalid Item")

    case _:
        print("Invalid Category")