with open('data/high_test.csv','r') as file:
    df = [float(line) for line in file]

print(len(df))
