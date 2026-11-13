n=5
for i in range(1,n+1):
    for j in range(i):
        if i==1 or i==2:
            print("*",end="")
    
        if i==3:
            if j==0 or j==2:
                print("*",end="")
            else:
                print(" ",end="") 
        if i==4:
            if j==0 or j==3:
                print("*",end="")
            else:
                print(" ",end="")
        if i==5:
            print("*",end="")   
    print()             


n = 5

for i in range(1, n+1):
    for j in range(i):
        if j == 0 or j == i-1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

