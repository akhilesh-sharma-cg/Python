score1 = int(input("Enter first score (0-100): "))

while score1 < 0 or score1 > 100:
    print("Invalid score. Try again.")
    score1 = int(input("Enter first score (0-100): "))

score2 = int(input("Enter second score (0-100): "))

while score2 < 0 or score2 > 100:
    print("Invalid score. Try again.")
    score2 = int(input("Enter second score (0-100): "))

score3 = int(input("Enter third score (0-100): "))

while score3 < 0 or score3 > 100:
    print("Invalid score. Try again.")
    score3 = int(input("Enter third score (0-100): "))

total = score1 + score2 + score3
average = total / 3

print("Total:", total)
print("Average:", average)