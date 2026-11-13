for i in range(1,6):
    for j in range(1,6):
        if (i/j)%2==0 or (i/j)==1 or (i/j)==i:
            j="X"
        else:
            j="-"   
        print(j,end=" ")
    print()         