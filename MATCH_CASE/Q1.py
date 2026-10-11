print("1.PIZZA \n2.BURGER \n3.PASTA \n4.SANDWICH")
num=int(input("ENTER A NUMBER WHICH PRODUCT YOU WANT:"))


match num:
    case 1:
        print("you have give order of pizza")
    case 2:
        print("you have give order of BURGER")
    case 3:
        print("you have give order of pasta")
    case 4:
        print("you have give order of Sandwich")
    case _:
        print("not a valid input please tryagain")       
            
           