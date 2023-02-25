from keras.layers import InputLayer
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
from keras.losses import MSE

model = Sequential()
model.add (InputLayer(input_shape=(2,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(3, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
opt = SGD(learning_rate=0.000001)
model.compile(loss=MSE,optimizer=opt)
model.fit(x,y)
