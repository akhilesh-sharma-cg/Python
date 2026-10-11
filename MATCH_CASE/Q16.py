print('1.Student\n2.Teacher')
num=int(input("enter a number"))

match num:
    case 1:
        print("1.View courses\n2.view marks\n3.View Attendence")
        number=int(input("ENTER A NUMBER:"))

        match number:
            case 1:
                print("Views Students")
            case 2:
                print("Enters Marks")   
            case 3:
                print("View Attendence")     


    case 2:
            print("1.View students\n2.view marks\n3.View Attendence")
            number=int(input("ENTER A NUMBER:"))
            match number:

                 case 1:
                     print("Views Students")
                 case 2:
                     print("Enters Marks")   
                 case 3:
                     print("View Attendence")       