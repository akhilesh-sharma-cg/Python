n = int(input("Enter a positive integer divisible by both 3 and 5: "))

while n <= 0 or n % 3 != 0 or n % 5 != 0:
    print("Invalid number! Please try again.")
    n = int(input("Enter a positive integer: "))

print("Accepted number:", n)