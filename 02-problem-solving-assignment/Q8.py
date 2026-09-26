budget=0
regular=0
premium=0
luxury=0
price=0
total=0
for i in range(1,9):
     price=(int(input("ENTER YOUR PRICE")))
     total+=  price
       


     if price<500:
        budget+=1
        
        
     elif 1999>=price>=500:
        regular+=1
          
     elif 4999>=price>=2000:
        regular+=1
        
     else:
        luxury+=1
print("total price:",total)
print("average price:",total/8)
print("Budget:",budget)
print("regular:",regular) 
print("premium:",premium)
print("luxuey:",luxury)
