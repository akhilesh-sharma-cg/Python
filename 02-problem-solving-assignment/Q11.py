for i in range(5):
    username = input("Enter username: ")

    length = len(username)
    digits = 0
    underscores = 0
    invalid = False

    for ch in username:
        if "0" <= ch <= "9":
            digits += 1
        elif ch == "_":
            underscores += 1
        elif ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
            pass
        else:
            invalid = True

    first = username[0]

    if not (("a" <= first <= "z") or ("A" <= first <= "Z")):
        result = "Invalid"
    elif invalid:
        result = "Invalid"
    elif length < 5 or length > 15:
        result = "Needs Improvement"
    elif digits == 0 or underscores == 0:
        result = "Needs Improvement"
    else:
        result = "Valid"

    print("Length:", length)
    print("First character:", first)
    print("Digits:", digits)
    print("Underscores:", underscores)
    print("Invalid special characters:", invalid)
    print("Classification:", result)
    