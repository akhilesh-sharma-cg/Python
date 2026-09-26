for i in range(1):
    b = input("ENTER A SENTENCE: ")
    a = len(b)
    vowel = 0
    consonants = 0

    for j in range(1, a+1):
        if b[j-1] in "aeiouAEIOU":
            vowel += 1
        else:
            consonants += 1

if vowel > consonants:
    print("vowel heavy")
elif vowel < consonants:
    print("consonants heavy")
else:
    print("balanced")