for i in range(1, 6):
    password = input("Enter password: ")
    count = 0

    if len(password) >= 8:
        count += 1

    for j in password:
        if j >= "A" and j <= "Z":
            count += 1
           

    for j in password:
        if j >= "a" and j <= "z":
            count += 1
            

    for j in password:
        if j >= "0" and j <= "9":
            count += 1
            

    for j in password:
        if not (j >= "A" and j <= "Z") and not (j >= "a" and j <= "z") and not (j >= "0" and j <= "9"):
            count += 1
            

    if count == 5:
        print("Strong")
    elif count >= 3:
        print("Medium")
    else:
        print("Weak")            

   


 

    
