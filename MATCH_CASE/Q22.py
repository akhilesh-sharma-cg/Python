

print("1.kilometers to Meters\n2.Meters to Kilometers\n3.Kilograms to Grams\n4.Grams to Kilograms")

num=int(input("ENTER A NUMBER WHICH OPERATION YOU WANT TO FOLLOW:"))

match num:
    case 1:
        number=int(input("ENTER A NUMBER in kilometer:"))
        output=number*1000
        print(output,"meter")
    case 2:
        number=int(input("ENTER A NUMBER in meter:"))
        output=number/1000
        print(output,"kilometers")  
    case 3:
         number=int(input("ENTER A NUMBER in kilograms:"))
         output=number*1000
         print(output,"grams")
    case 4:
        number=int(input("ENTER A NUMBER in Grams:"))
        output=number/1000
        print(output,"kilograms") 
    case 5:
        print("invalid input \nplease tey again")



