word = "ABCD"
n = 4

for i in range(n):
    for j in range(1, n+1):
        print(word[i] + str(j), end=" ")
    print()