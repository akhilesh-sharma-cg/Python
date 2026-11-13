str = input("ENTER A STRING:").lower()

for i in str:
    for j in str:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u") and (j != "a" and j != "e" and j != "i" and j != "o" and j != "u"):
            print(i, "-", j)