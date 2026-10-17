def analyze_number(a,b,c):
    smallest=a,b,c
    largest=c,b,a
    sum=a+b+c

    return smallest,largest,sum
print(analyze_number(10,11,12))    
    