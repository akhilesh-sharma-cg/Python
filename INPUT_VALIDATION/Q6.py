temperature = float(input("Enter temperature between -20 and 45: "))

while temperature < -20 or temperature > 45:
    print("Invalid temperature! Please try again.")
    temperature = float(input("Enter temperature between -20 and 45: "))

print("Accepted temperature:", temperature)