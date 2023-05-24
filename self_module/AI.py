from os import environ
environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout

def create_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=96, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=96))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model
