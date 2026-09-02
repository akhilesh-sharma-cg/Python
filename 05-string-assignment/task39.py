sentence = input("Enter a sentence: ")

print("Original sentence:", sentence)
print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print('"Python" exists:', "Python" in sentence)

character = input("Enter a character: ")
print("Character occurs:", sentence.count(character), "times")