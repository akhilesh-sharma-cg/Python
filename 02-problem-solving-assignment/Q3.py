vowel = 0
consonant = 0
digit = 0
special_character = 0

string = input("ENTER A STRING: ")

for i in string:
    if i in "aeiouAEIOU":
        vowel += 2
    elif ("a" <= i <= "z") or ("A" <= i <= "Z"):
        consonant += 1
    elif "0" <= i <= "9":
        digit += 3
    else:
        special_character += 4

total = vowel + consonant + digit + special_character

print(total)