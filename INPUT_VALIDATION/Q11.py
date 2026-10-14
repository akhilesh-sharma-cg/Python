
n = int(input("Enter an integer between 10 and 50: "))

while n < 10 or n > 50:
    print("Invalid number! Please try again.")
    n = int(input("Enter an integer between 10 and 50: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")