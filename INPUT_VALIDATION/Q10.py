pin=2459
i=0
while i<3:
    enter=int(input("ENTER YOUR PIN:"))
    if pin==enter:
        print("succesfully login")
    else: print("try again")    
    i+=1
print("reconnect after 30 min ")    