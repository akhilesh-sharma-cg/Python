age = int(input("Enter your age: "))

while age < 0 or age > 120:
    print("Invalid age! Please try again.")
    age = int(input("Enter your age: "))

print("Accepted age:", age)