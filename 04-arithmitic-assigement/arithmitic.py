a = 10
b = 3

print( a + b)
print( a - b)
print( a * b)
print( a / b)
print( a // b)
print(a % b)
print(a ** b)




a = 10
b = 3.5

print(a + b, type(a + b))
print(a - b, type(a - b))
print(a * b, type(a * b))
print(a / b, type(a / b))
print(a // b, type(a // b))
print(a % b, type(a % b))
print(a ** b, type(a ** b))



marks1 = 80
marks2 = 75
marks3 = 90

total = marks1 + marks2 + marks3
average = total / 3

print("Total:", total)
print("Average:", average)




price = 100
quantity = 3

total_price = price * quantity

print("Total price:", total_price)




#distinguse between even and odd is simple if we divide the number with 2 and give reminder 1 than it is odd and also if we get reminder 0 then it is even.


num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")




    a = 10
b = 3

print("Normal division:", a / b)
print("Floor division:", a // b)

a = -10
b = 3

print("Normal division:", a / b)
print("Floor division:", a // b)




a = -10
b = -3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)


print( 10 - 5)
print( 10 - (-5))
print( -10 - 5)
print( -10 - (-5))




print( 10 // 3)
print( -10 // 3)
print( 10 // -3)
print( -10 // -3)




print( 10 % 3)
print(-10 % 3)
print( 10 % -3)
print(-10 % -3)




print(10 + 5 * 2)        # 20  
print(20 - 4 / 2)        # 18.0 
print(10 + 20 / 5 * 2)   # 18.0 
print(2 + 3 * 4 ** 2)    # 50 
print(100 - 20 // 5)     # 96 


print(10 + 5 * 2)        # 20
print((10 + 5) * 2)      # 30

print(20 - 10 / 2)       # 15.0
print((20 - 10) / 2)     # 5.0

print(2 + 3 * 4)         # 14
print((2 + 3) * 4)       # 20




a = True
b = False

print(a + b, type(a + b))
print(a - b, type(a - b))
print(a * b, type(a * b))
print(a / b, type(a / b))
print(a // b, type(a // b))
print(a % b, type(a % b))
print(a ** b, type(a ** b))



print(True + 5)    # 6
print(False + 5)   # 5
print(True * 10)   # 10
print(False * 10)  # 0
print(True - 5)    # -4
print(False - 5)   # -5


first_name = "Akhilesh"
last_name = "Sharma"

full_name = first_name + " " + last_name

print(full_name)


#in this question only integer can give answer

word = "Hello"

print(word * 3)

print(word * 2.5)



a = "Hello"
b = "World"

print(a + b)   # Works
print(a - b)   # Error
print(a * 3)   # Works
print(a / b)   # Error


value = None
num = 5

print(value + num)
print(value - num)
print(value * num)
print(value / num)
print(value // num)
print(value % num)
print(value ** num)



# Division by Zero
a = 10
b = 0
print(a / b)
# Error: ZeroDivisionError


# Invalid String Arithmetic
a = "Hello"
b = "World"
print(a - b)
# Error: TypeError


# Arithmetic with None
value = None
num = 5
print(value + num)
# Error: TypeError



a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)



a = 10
b = -3
c = 2.5

print("1.", a + b)           # 7
print("2.", a - c)           # 7.5
print("3.", a * b)           # -30
print("4.", a / c)           # 4.0
print("5.", a // b)          # -4
print("6.", a % b)           # -2
print("7.", a ** 2)          # 100
print("8.", (a + b) * c)     # 17.5
print("9.", a + b * c)       # 2.5
print("10.", (a - b) / c)    # 5.2
print("11.", a + c * b)      # 2.5
print("12.", (a ** 2) // c)  # 40.


