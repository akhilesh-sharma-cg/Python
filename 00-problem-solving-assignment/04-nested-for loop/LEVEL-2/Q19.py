n=int(input("ENTER A NUMBER:"))
for i in range(n):
    for j in range(1,n):
        if(i*j)%2==0:
            print(i,j,i*j)
        else:
            continue
            
