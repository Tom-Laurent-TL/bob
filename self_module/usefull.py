# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:51:44 2021

@author: Tom
"""

def dist(x,y):
    sqrt2 = 1.4142135623730950488016887242097
    return abs(x-y)/sqrt2

def model_variance(y_test,predictions):
    ds = []
    for i in range(0,len(y_test)):
        d = dist(y_test[i],predictions[i])
        if y_test[i] != 0:
            ds.append(d/y_test[i])
        else:
            ds.append(d)
    return sum(ds)/len(ds)

def model_delta(y_test,predictions):
    deltas = []
    for i in range(0,len(y_test)):
        delta = abs(y_test[i]-predictions[i])
        deltas.append(delta)
    return sum(deltas)/len(deltas)
