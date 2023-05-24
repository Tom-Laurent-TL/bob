from math import copysign

sign = lambda x: copysign(1, x)

def score(tab):
    link=0
    for i in range(2,len(tab)):
        if sign(tab[i]-tab[i-1]) == sign(tab[i-1]-tab[i-2]):
            link+=1
    return link/(len(tab)-2)


file = open('data/predictions.csv','r')
predictions = [float(line) for line in file]
del file

correlation = score(predictions)
print(round(correlation*100,2),'%')
