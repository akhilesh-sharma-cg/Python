print("YOUR BALANCE IN BANK IS ₹5000")
rupess=int(input("ENTER A AMOUNT YOU WANT TO WITHDRAW:"))

while rupess>5000 or rupess<=0:
    print("INVALID AMOUNT,PLEASE TRY AGAIN")
    rupess=int(input("ENTER A AMOUNT YOU WANT TO WITHDRAW:"))
print("amount succesfully withdraw")    