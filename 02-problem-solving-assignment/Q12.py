sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

a = 0
e = 0
i = 0
o = 0
u = 0

for ch in sentence:

    if ch in "aeiouAEIOU":
        vowels += 1

        if ch == "a" or ch == "A":
            a += 1
        elif ch == "e" or ch == "E":
            e += 1
        elif ch == "i" or ch == "I":
            i += 1
        elif ch == "o" or ch == "O":
            o += 1
        elif ch == "u" or ch == "U":
            u += 1

    elif ch >= "a" and ch <= "z" or ch >= "A" and ch <= "Z":
        consonants += 1


print("Vowels:", vowels)
print("Consonants:", consonants)

if vowels > consonants:
    print("Vowels Win")
elif consonants > vowels:
    print("Consonants Win")
else:
    print("Draw")

print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)