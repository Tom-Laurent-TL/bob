import matplotlib.pyplot as plt
from math import copysign

sign = lambda x: copysign(1, x)

def score(tab):
    link=0
    for i in range(2,len(tab)):
        if sign(tab[i]-tab[i-1]) == sign(tab[i-1]-tab[i-2]):
            link+=1
    return link/(len(tab)-2)

with open('data/high_test.csv','r') as file:
    df = [float(line) for line in file]


nb_points = int(len(df)/50)-1
nb_points = min(101, nb_points)
nb_points *= 5
df = df[-nb_points:]
blank = [None for value in df]

with open('data/predictions.csv','r') as file:
    predictions = [float(line) for line in file]

score_marche = score(df[-len(predictions):])
score_predictions = score(predictions)

predictions = blank + predictions

plt.style.use('dracula')
plt.title('score : '+str(round(score_marche*score_predictions*100)))
plt.plot(predictions)
plt.plot(df)
plt.show()
