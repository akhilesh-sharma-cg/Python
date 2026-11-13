rows=int(input("ENTER THE NUMMBER OS ROWS"))
col=int(input("ENTER THE NUMMBER OS col"))
for i in range(rows):
    for j in range(col):
        if j%2==0:
            print(j,end=" ")
        else:
            pass    
    print()