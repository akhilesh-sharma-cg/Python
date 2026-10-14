username = input("Enter username: ").strip()

while len(username) < 5 or username == "" or " " in username:
    print("Invalid username! Try again.")
    username = input("Enter username: ").strip()

print("Accepted username:", username)