print("1.Wi-Fi\n 2.BLUETHOOTH\n3.MOBILE DATA\n 4.AIRPLANE MODE \n5.EXIT")
num=int(input("ENTER A NUMBER YOU WANT TO ADD IN MOBILE MENU:"))


match num:
    case 1:
        print(" Wi-Fi")
    case 2:
        print(" Bluetooth")
    case 3:
        print(" Bluetooth")
    case 4:
        print("Airplane Mode")
    case 5:
        print("Exit")    
    case _:
        print("invalid setting")       
            