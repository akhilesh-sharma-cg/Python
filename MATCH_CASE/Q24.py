print("1.Start Exam\n2.View Result\n3.Exit")
number=int(input("ENTER A NUMBER WHICH YOU WANT TO SELECT:"))
age=int(input("ENTER YOUR AGE:"))

match number:
    case 1:
        if age>18:
            print(age)
            print("YOU CAN START THE EXAM")  
        else:
            print("you are not able to start the exam because your age is not valid")          
    
    case 2:
        print("view result")
    case 3:
        print("Exit")    

    case _:
        print("enter a vlaid number please try agaiin")    