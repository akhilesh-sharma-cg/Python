print("1. Student")
print("2. Teacher")
print("3. Administration")

role = int(input("Enter role: "))

match role:
    case 1:
        print("1. Profile")
        print("2. Marks")
        print("3. Attendance")
        print("4. Courses")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Choice")

    case 2:
        print("1. Students")
        print("2. Enter Marks")
        print("3. Attendance")
        print("4. Courses")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Choice")

    case 3:
        print("1. Fees")
        print("2. Admissions")
        print("3. Notices")
        print("4. Departments")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Administration Fees")
            case 2:
                print("Opening Administration Admissions")
            case 3:
                print("Opening Administration Notices")
            case 4:
                print("Opening Administration Departments")
            case _:
                print("Invalid Choice")

    case _:
        print("Invalid Role")