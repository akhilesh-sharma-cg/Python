N = int(input("Enter N: "))

for i in range(N):
    for j in range(N):
        if i == j:
            print("SPECIAL", end=" ")
        elif i + j == N:
            print("PAIR", end=" ")
        else:
            print("NORMAL", end=" ")
    print()