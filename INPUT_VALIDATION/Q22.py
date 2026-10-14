num = int(input("Enter an integer from 1 to 10: "))

while num < 1 or num > 10:
    print("Invalid input. Try again.")
    num = int(input("Enter an integer from 1 to 10: "))

print("Valid number:", num)