for i in range(5):
    for j in range(5):
        if (i+j)%2==0:
            j="E"
        else:
            j="O" 
        print(j,end=" ") 
    print()          