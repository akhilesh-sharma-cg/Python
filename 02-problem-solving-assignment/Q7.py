
string=input("ENTER A STRING:")

for i in string:
    count=0

    for j in string:
        if j==i:
             count+=1

if count>=4:
    print("highly repeated:",i) 
elif count >= 3:
    print("repeadetd",i)
else:
    print("Duplicate",i)    