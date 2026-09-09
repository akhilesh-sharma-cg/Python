age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

if 18 <= age <= 25 and marks >= 85 and attendance >= 75 and income <= 300000:
    print("Scholarship granted")
else:
    print("Scholarship not granted")

