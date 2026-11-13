str = input("ENTER A STRING:")

for i in str:
    for j in str:
        if (i >= "A" and i <= "Z") and (j >= "A" and j <= "Z"):
            print(i, j)
        elif (i >= "a" and i <= "z") and (j >= "a" and j <= "z"):
            print(i, j)