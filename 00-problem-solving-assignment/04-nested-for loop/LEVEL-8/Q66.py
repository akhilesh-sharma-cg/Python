r=4
c=5
for i in range(r):
    for j in range(c):
        if i==0 or i==3:
            print("*",end="")    
        if i==1 or i==2: 
            if j==1 or j==2 or j==3:
                print(" ",end="")  
            else:
                print("*",end="")      
    print()        