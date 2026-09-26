highest_marks = -1
highest_name = ""

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    # Grade
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    # Count vowels
    vowels = 0

    for j in name:
        if j in "aeiouAEIOU":
            vowels += 1

    # Count characters
    characters = len(name)

    # Count consonants
    consonants = characters - vowels

    print("Grade:", grade)
    print("Vowels:", vowels)
    print("Characters:", characters)
    print("Consonants:", consonants)

    if vowels > consonants:
        print("More vowels")
    elif consonants > vowels:
        print("More consonants")
    else:
        print("Vowels and consonants are equal")

    # Highest marks
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

    print()

print("Student with highest marks:", highest_name)
print("Highest marks:", highest_marks)   


