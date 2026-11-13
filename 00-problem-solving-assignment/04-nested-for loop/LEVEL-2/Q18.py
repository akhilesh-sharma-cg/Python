n=int(input("ENTER A NUMBE:"))
for i in range(1,n):
    for j in range(1,n):
        if (i+j)>=n:
            print(i ,j)
        else:
            continue        