sen=input("ENTER A SENTENCE:").split()
for i in range(len(sen)-1):
        if sen[i][-1]==sen[i+1][-1]:
            print(sen[i],sen[i+1])
