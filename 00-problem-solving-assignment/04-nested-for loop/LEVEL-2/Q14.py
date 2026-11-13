for i in range(5):
    for j in range(5):
        if i==j:
            j="Same"
        else:
            j="Different"
        print(j,end=" ") 
    print()               