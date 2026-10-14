password=input("ENTER YOUR PASSWORD:").strip().lower()
a=len(password)
while a<8:
    print("PASSWORD ATLEAST CONTAIN MORE THAN 8 CHARCATER")
    password=input("ENTER YOUR PASSWORD:").strip()

    a=len(password)

print("you have enter correct password")    


