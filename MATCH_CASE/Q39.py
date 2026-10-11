print("1.Employee\n2.Manager")
number=int(input("ENTER A NUMBER WHICH YOU ARE CURRENTLY IN WORK:"))

match number:
    case 1:  
        print("1.View profile\n2.Apply leave\n3.View Salary") 
        number=int(input("ENTER A NUMBER WHICH CATERORY YOU WANT TO SEE:")) 
        match number:
            case 1:
                 print("View profile")

            case 2:
              apply_leave=int(input("ENTER A NUMBER OF DAY YOU WANT LEAVE:"))
              if apply_leave>0:
                print("leave request Submitted")
              else:
                print("INVALID LEAVE DAY")  



            case 3:
              print("view salary")  
            case _:
                print("ENTER A VALID NUMBER")  

    case 2:
        print("1.View team\n2.Approve leave\n3.view report ")  
        number=int(input("ENTER A NUMBER YOU WANT TO VISITE:"))     

        match number:
            case 1:  
                print("View team")  
                print("akhilesh,ved,het,lavya")
            case 2:        
                print("approve leave")
            case 3:
                print("VIEW REPORTS") 
            case _:
                print("invalid number") 

    case _:
        print("enter a valid number") 