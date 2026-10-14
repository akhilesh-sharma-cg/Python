marks=int(input("ENTER YOUR MARKS:"))

while marks<=0 or marks>100:
    marks=int(input("ENTER YOUR MARKS:"))
    print("invalid marks ,try again")

print("marks submitted")