from os import environ
environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import matplotlib.pyplot as plt


scaler = MinMaxScaler(feature_range=(0,1))

with open('data/high_test.csv','r') as file:
    df = [float(line) for line in file]

nb_points = int(len(df)/50)-1
nb_points = min(101, nb_points)

df.reverse()
df = np.array(df)
df = df.reshape(-1, 1)
df = scaler.fit_transform(df)


X = [[] for i in range(nb_points)]

def average(lst):
    return sum(lst)/len(lst)

for period in range(1,nb_points+1):
    for i in range(0,period*50,period):
        X[period-1].append(average(df[i:i+period]))

for x in X:
    x.reverse()

X = np.array(X)


model = load_model('model/model.h5')
predictions = model.predict(X)
predictions = scaler.inverse_transform(predictions)

file = open('data/predictions.csv','w')
for prediction in predictions:
    file.write(str(prediction[-1])+'\n')
file.close()
