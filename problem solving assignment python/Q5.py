n1=int(input("ENTER A NUMBER:"))
n2=int(input("ENTER A NUMBER:"))
n3=int(input("ENTER A NUMBER:"))

if n1>n2>n3 or n1>n3>n2:
    print("n1 is the greatesr number")

elif n2>n1>n3 or n2>n3>n1:
    print("n2 is the greatest number")
else:
    print("n3 is the greatest number")    
