n1=int(input("ENTER A NUMBER:"))
n2=int(input("ENTER A NUMBER:"))
n3=int(input("ENTER A NUMBER:"))

if n1>n2>n3 or n2>n1>n3:
    print("n3 is the smallest number")

elif n3>n2>n1 or n2>n3>n1:
    print("n1 is the smallest number")
else:
    print("n2  is the smallest number")    
