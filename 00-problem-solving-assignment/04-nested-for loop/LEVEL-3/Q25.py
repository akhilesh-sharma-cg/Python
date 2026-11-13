str=input("enter a string:")
string=input("enter a string:")
count=0
for i in str:
    for j in string:
        if i==j:
            count+=1
        else:
            pass
print(count)
