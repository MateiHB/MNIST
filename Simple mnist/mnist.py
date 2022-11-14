# -*- coding: utf-8 -*-
"""MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qaAVKKSpJNm7OzbrqwuSA_eUYtECJpiB
"""

from keras.datasets import mnist
from matplotlib import pyplot
import tensorflow as tf

#Loading data from MNIST dataset
(train_x, train_y), (test_x, test_y) = mnist.load_data()

print('x_train: ' + str(train_x.shape))
print('y_train: ' + str(train_y.shape))
print('x_test:  '  + str(test_x.shape))
print('y_test:  '  + str(test_y.shape))

#Normalizing the data
train_x = train_x/255

pyplot.imshow(train_x[0])

#Showing the first 9 examples from the training dataset
fig, ax = pyplot.subplots(3, 3)
ax[0, 0].imshow(train_x[0], cmap=pyplot.get_cmap('gray'))
ax[0, 1].imshow(train_x[1], cmap=pyplot.get_cmap('gray'))
ax[0, 2].imshow(train_x[2], cmap=pyplot.get_cmap('gray'))
ax[1, 0].imshow(train_x[3], cmap=pyplot.get_cmap('gray'))
ax[1, 1].imshow(train_x[4], cmap=pyplot.get_cmap('gray'))
ax[1, 2].imshow(train_x[5], cmap=pyplot.get_cmap('gray'))
ax[2, 0].imshow(train_x[6], cmap=pyplot.get_cmap('gray'))
ax[2, 1].imshow(train_x[7], cmap=pyplot.get_cmap('gray'))
ax[2, 2].imshow(train_x[8], cmap=pyplot.get_cmap('gray'))
pyplot.show()

#First model
#Classical model using simple dense hidden layers
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(128, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'softmax')
])

#Setting the opitimizer and loss function
model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

#Training the model with the training dataset
model.fit(train_x, train_y, epochs = 5)

#Predicting digits for testing dataset
val_loss, val_acc = model.evaluate(test_x, test_y)
print("Achieved accuracy for first model: " + str(val_acc))

#Second model
#Convolutional model using convolutional and dense hidden layers
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation = 'relu', input_shape = (28,28,1)),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation = 'relu'),
    tf.keras.layers.Dense(10, activation = 'softmax')
])

#Setting the opitimizer and loss function
model.compile(optimizer = 'rmsprop',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

#Training the model with the training dataset
model.fit(train_x, train_y, epochs = 5, batch_size = 64)

#Predicting digits for testing dataset
val_loss, val_acc = model.evaluate(test_x, test_y)
print("Achieved accuracy for second model: " + str(val_acc))