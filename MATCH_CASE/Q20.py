print("1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION:")
operation=input("ENTER A NUMBER WHICH OPERATION YOU WANT TO FOLLOW:")
a=int(input("ENTER A NUMBER:"))
b=int(input("ENTER A NUMBER:"))
num=int(input("ENTER A case which you want to perform:"))

match num:
    case 1:
        print("RESULT:",a+b)
    case 2:
        print("RESULT",a-b)
    case 3:
        print("RESULT",a*b)   
    case 4:
        print("RESULT",a/b)    
    case _:
        print("not a valid input try again")         