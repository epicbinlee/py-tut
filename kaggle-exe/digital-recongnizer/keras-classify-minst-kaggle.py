import pandas as pd
from keras.optimizers import Adam
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.models import Sequential
from keras.utils import np_utils
from keras.datasets import mnist
import numpy as np
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
np.random.seed(1337)
dir = r'/Users/leebin/proj/py_collection/py-tut/kaggle-exe/digital-recongnizer/data/'
train_path = dir + r'train.csv'
test_path = dir + r'test.csv'
submit_path = dir + r'sample_submission.csv'
train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)
submit_data = pd.read_csv(submit_path)
# 判断是不是灰度图
max(train_data[max(train_data)])
# test不包含标签，先需要归一化处理
test_data = test_data / 255.0
max(train_data[max(train_data)])
X_train = train_data.drop(['label'], axis=1)
y_train = train_data['label']
X_test = test_data
# train去掉标签后,需要归一化处理
X_train = X_train / 255.0
print(X_train.columns)
print(y_train)
max(X_test[max(X_test)])
X_train = X_train.values.reshape(-1, 1, 28, 28)
X_test = X_test.values.reshape(-1, 1, 28, 28)
y_train = np_utils.to_categorical(y_train, num_classes=10)

model = Sequential()
model.add(Convolution2D(batch_input_shape=(None, 1, 28, 28), filters=32, kernel_size=5, strides=1, padding='same', data_format='channels_first', ))
model.add(MaxPooling2D(pool_size=2, strides=2, padding='same', data_format='channels_first', ))
model.add(Convolution2D(64, 5, strides=1, padding='same', data_format='channels_first'))
model.add(Activation('relu'))
model.add(MaxPooling2D(2, 2, 'same', data_format='channels_first'))
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
adam = Adam(lr=1e-4)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, batch_size=100)
r = model.predict_classes(X_test)
print(r)
submissions = pd.DataFrame({"ImageId": list(range(1, len(r) + 1)), "Label": r})
print(submissions)
submissions.to_csv("DR.csv", index=False, header=True)
