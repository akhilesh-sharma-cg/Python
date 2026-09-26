string = input("Enter a string: ")

vowel = 0
consonant = 0
digit = 0
special = 0

for i in range(len(string)):
    j = string[i]

    if i % 2 == 0:
        position = "Even"
    else:
        position = "Odd"

    if j in "aeiouAEIOU":
        category = "Vowel"
        vowel += 1
    elif j >= "a" and j <= "z" or j >= "A" and j <= "Z":
        category = "Consonant"
        consonant += 1
    elif j >= "0" and j <= "9":
        category = "Digit"
        digit += 1
    else:
        category = "Special Character"
        special += 1

    print(j, "Position:", i, position, category)

print("Vowels:", vowel)
print("Consonants:", consonant)
print("Digits:", digit)
print("Special Characters:", special)