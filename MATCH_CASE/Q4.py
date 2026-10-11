trffic_light=input("ENTER A COLOR OF LIGHT:")   

match trffic_light:
    case "red":
        print("stop")
    case "yellow":
        print("wait")  
    case "green":
        print("Go")  
    case _:
        print("Invalid Signal")        
            