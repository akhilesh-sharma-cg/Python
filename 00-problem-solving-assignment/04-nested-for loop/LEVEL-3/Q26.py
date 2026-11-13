str=input("ENTER A STRING:")
for i in range(len(str)):
    count=0 
    for j in range(len(str)):
        if str[i]==str[j]:
            count+=1
    print(str[i],count)      
               
    