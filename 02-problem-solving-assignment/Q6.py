

for i in range(1,6):
    number=int(input("enter a number"))
    count=0
    even=0
    odd=0
    equal=0
    text=str(number)
    for j in text:
        if int(j)%2==0:
            even+=1
        elif int(j)%2==1:
            odd+=1

    if odd>even:
        print("odd")
    elif even>odd:
        print("even") 
    else:
        print("equal")     



     