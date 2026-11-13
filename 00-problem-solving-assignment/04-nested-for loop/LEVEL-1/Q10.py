num=int(input("ENTER A NUMBER:"))
for i in range(num):
    for j in range(num):
        if j%2==0:
            j="0"
        else:
            j="1" 
        print(j,end="")
    print()           