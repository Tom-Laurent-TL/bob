with open('data/high_train.csv','r') as file:
    data = [float(line) for line in file]

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

X = []
Y = []

for period in range(1, 61):
    rescaled = rescale(data,period)
    train, test = splitTT(rescaled,50)
    for i in range(0,len(train)):
        X.append(train[i])
        Y.append(test[i])
