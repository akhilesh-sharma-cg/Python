n = int(input("Enter an integer between 1 and 100: "))

while n < 1 or n > 100:
    print("Invalid number! Please try again.")
    n = int(input("Enter an integer between 1 and 100: "))

print("Accepted number:", n)