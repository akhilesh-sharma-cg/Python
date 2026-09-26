for i in range(1):
    a=input("ENTER A SENTANCE:")
    b=len(a)
    Uppercase=0
    Lowercase=0
    Digits=0
    Special_characters=0

    for j in range(1,b+1):
         if "A" <= a[j-1] <= "Z":
            Uppercase += 1

         elif "a" <= a[j-1] <= "z":
            Lowercase += 1

         elif "0" <= a[j-1] <= "9":
            Digits += 1

         else:
            Special_characters += 1
percentageupper=Uppercase/4
percentagelower=Lowercase/4
percentagedigit=Digits/4
percentagespecial_character=Special_characters/4

print("uppercase/4:",percentageupper) 
print("lowercase/4:",percentagelower) 
print("digit/4:",percentagedigit) 
print("special_character/4:",percentagespecial_character)                

