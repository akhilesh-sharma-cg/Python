print("1.VIEW PROFILE\n 2.VIEW COURSES\n3.VIEW MARKS\n 4.VIEW ATTENDENCE \n5.LOGOUT ")
num=int(input("enter a number:"))
match num:
    case 1:
        print("view profile")
    case 2:
        print("View courses")
    case 3:
        print("View marks")  
    case 4:
        print("view attendence")  
    case 5:
        print("logout")     
    case _:
        print("enter a valid number")           