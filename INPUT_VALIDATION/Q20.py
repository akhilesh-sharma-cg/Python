count = int(input("How many numbers do you want to enter (1-20)? "))

while count < 1 or count > 20:
    print("Invalid count. Enter a number from 1 to 20.")
    count = int(input("How many numbers do you want to enter (1-20)? "))

total = 0

for i in range(count):
    num = float(input("Enter a number: "))
    total = total + num

average = total / count

print("Average:", average)