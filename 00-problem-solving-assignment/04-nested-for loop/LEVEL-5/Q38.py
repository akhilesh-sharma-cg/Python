sen=input("ENTER A SENTENCE:").split()
for i in range(len(sen)-1):
        if sen[i][0]==sen[i+1][0]:
            print(sen[i],sen[i+1])
