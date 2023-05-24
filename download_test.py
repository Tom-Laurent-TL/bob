import pandas as pd
from binance.client import Client
#import ta
#import matplotlib.pyplot as plt

client = Client()

klinesT = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_1MINUTE, "6 day ago UTC")

df = pd.DataFrame(klinesT, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
df['high'] = pd.to_numeric(df['high'])

df = df.set_index(df['timestamp'])
df.index = pd.to_datetime(df.index, unit='ms')
del df['timestamp']
high = df['high']

file = open('data/high_test.csv','w')

for value in high.values:
    file.write(str(value)+'\n')

file.close()
