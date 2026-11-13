sen=input("ENTER A SENTENCE:").split()
for i in range(len(sen)-1):
    if len(sen[i])==len(sen[i+1]):
        print(sen[i],sen[i+1])
    