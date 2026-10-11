print("1.CHECK BALANCE\n 2.WITHDRAW MONEY\n3.DEPOSITE MONEY\n 4.CHNAGE PIN \n5.EXIT")
num=int(input("ENTER A NUMBER YOU WANT TO ADD IN MOBILE MENU:"))


match num:
    case 1:
        print(" CHECK BALANCE")
    case 2:
        print(" WITHDRAW MONEY")
    case 3:
        print("DEPOSITE MONEY")
    case 4:
        print("CHNAGE PIN")
    case 5:
        print("Exit")    
    case _:
        print("invalid setting")       