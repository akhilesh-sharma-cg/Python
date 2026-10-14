num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")

while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operator. Try again.")
    operator = input("Enter operator (+, -, *, /): ")

num2 = float(input("Enter second number: "))

while operator == "/" and num2 == 0:
    print("Division by zero is not allowed.")
    num2 = float(input("Enter second number again: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2

print("Result:", result)