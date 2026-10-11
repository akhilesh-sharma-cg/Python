print("1. Morning Show\n2. Afternoon Show\n3. Evening Show\n4. Night Show")

match show:
    case 1:
        print("Morning Show Selected")
    case 2:
        print("Afternoon Show Selected")
    case 3:
        print("Evening Show Selected")
    case 4:
        print("Night Show Selected")
    case _:
        print("Invalid Show")