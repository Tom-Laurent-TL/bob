# -*- coding: utf-8 -*-

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from self_module.AI import create_model


with open('data/high_train.csv','r') as file:
    df = [float(line) for line in file]

def average(lst):
    return sum(lst) / len(lst)

def splitTT(lst, period):
    train = [lst[x:x+period] for x in range(0, len(lst) - len(lst)%period - period, period)]
    test = [lst[x+period] for x in range(0, len(lst) - len(lst)%period - period, period)]
    return train, test

def rescale(lst, period):
    return [average(lst[x:x+period]) for x in range(0, len(lst) - len(lst)%period, period)]

def answer(lst, period):
    return [lst[x+period] for x in range(0, len(lst), period)]

scaler = MinMaxScaler(feature_range=(0,1))

df = np.array(df)
df = df.reshape(-1, 1)
df = scaler.fit_transform(df)

df = [i for i in df]

X = []
Y = []

for period in range(1, 101):
    rescaled = rescale(df,period)
    train, test = splitTT(rescaled,50)
    for i in range(0,len(train)):
        X.append(train[i])
        Y.append(test[i])

X = np.array(X)
Y = np.array(Y)
Y = Y.reshape(-1, 1)
Y = scaler.fit_transform(Y)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.001, shuffle=True)

model = create_model((x_train.shape[1], 1))
model.fit(x_train, y_train, epochs=10, batch_size=32)
model.save('model/model.h5')
