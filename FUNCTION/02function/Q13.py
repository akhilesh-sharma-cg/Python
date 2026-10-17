def classify(number):
    if number>0:
        return "positive"
    elif number<0:
        return "negative"   
    else:
        return "zero" 
print(classify(50))           