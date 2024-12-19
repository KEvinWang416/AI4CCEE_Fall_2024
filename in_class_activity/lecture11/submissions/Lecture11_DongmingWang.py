# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v7A4T3tqsElgyuBAuJJexqDer4ZJTpgj
"""

pip install tensorflow

# prompt: Import the datasets module from tensorflow.keras. This will allow you to load the CIFAR-10
# dataset

!pip install tensorflow

from tensorflow.keras.datasets import cifar10

# Now you can use the cifar10 module
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# prompt: Use the datasets.cifar10.load_data() method to download and load the CIFAR-10 dataset

from tensorflow.keras.datasets import cifar10

# Now you can use the cifar10 module
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# prompt: Assign the result to two tuples:
# • (train_images, train_labels) for the training data.
# • (test_images, test_labels) for the testing data.

train_images, train_labels = x_train, y_train
test_images, test_labels = x_test, y_test

# prompt: Pixel values in the CIFAR-10 images range from 0 to 255. Normalize these values to a range of 0
# to 1 to improve model performance.

train_images = train_images / 255.0
test_images = test_images / 255.0

# prompt: Divide both train_images and tPixel values in the CIFAR-10 images range from 0 to 255.
# Normalize these values to a range of 0 to 1 to improve model performance.

train_images = train_images / 255.0
test_images = test_images / 255.0

# prompt: Divide both train_images and test_images by 255.0. Update their values directly

x_train = x_train / 255.0
x_test = x_test / 255.0

# prompt: Verify the download process

import matplotlib.pyplot as plt
plt.imshow(x_train[0])
plt.show()
print(y_train[0])
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
y_test.shape

# prompt: Create a list named class_names containing the names of the classes. These should correspond to
# the classes in the dataset, such as =
# ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck’]

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# prompt: Use plt.figure() to create a figure for the plot. Set its size to 10x10 using the figsize parameter.

plt.figure(figsize=(10, 10))
plt.imshow(x_train[0])
plt.show()

# prompt: Loop through the first 25 images Using a for loop with a range of 25. This will help in plotting 25
# images (from 0 to 24).

import matplotlib.pyplot as plt

# Assuming x_train is already loaded and preprocessed as in the provided code

plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i])
    plt.xlabel(class_names[y_train[i][0]])
plt.show()

# prompt: Create a subplot for each image. Inside the loop, use plt.subplot(rows, cols, index) to
# create a grid layout of 5 rows and 5 columns. Use i+1 as the index to position each image
# correctly in the grid.

plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i])
    plt.xlabel(class_names[y_train[i][0]])
plt.show()

# prompt: Remove axis ticks and grid:
# 1. For a clean visual appearance, use plt.xticks([]) and plt.yticks([]) to remove ticks from both axes.
# 2. Use plt.grid(False) to disable the grid.

# The provided code already includes the necessary lines to remove axis ticks and grid.
# plt.xticks([])
# plt.yticks([])
# plt.grid(False)
# These lines are present within the loop that plots the images.  No further code is needed.

# prompt: Display the image:
# 1. Use plt.imshow() to display each image from the dataset (train_images[i]).

import matplotlib.pyplot as plt
import numpy as np

# Assuming x_train, y_train, and class_names are already defined as in the previous code.

# Display the first 25 images from the training set.
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary) # Added cmap for better visualization if needed
    plt.xlabel(class_names[y_train[i][0]])
plt.show()

# prompt: Add a label:
# 1. Use plt.xlabel() to display the class name below each image. Access the class name using the label
# index from train_labels[i][0].

# Assuming x_train, y_train, and class_names are already defined as in the previous code.

# Display the first 25 images from the training set.
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary) # Added cmap for better visualization if needed
    plt.xlabel(class_names[y_train[i][0]])
plt.show()

# prompt: Call plt.show() to render the grid of images and their respective labels

# The code already calls plt.show() at the end of the plotting loop.
# No further code is needed to render the grid of images and their labels.

# prompt: Import the necessary modules:
# • Use the Sequential model class from tensorflow.keras.models.
# • Use the Conv2D and MaxPooling2D layers from tensorflow.keras.layers

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D

# prompt: Define a sequential model:
# • Create an instance of the Sequential model using models.Sequential().

model = Sequential()

# prompt: Add the first convolutional layer:
# • Add a Conv2D layer to the model using the add() method.
# • Configure the layer with the following parameters:
# • Filters: 32 (number of output filters in the convolution).
# • Kernel size: (3, 3) (dimensions of the filter).
# • Activation function: 'relu' (rectified linear unit).
# • Input shape: (32, 32, 3) (input images with height, width, and color channels).

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))

# prompt: Use model.summary():
# • Call the summary() method on the model to print its architecture. This shows the structure and
# parameters of the model.

model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.summary()

# prompt: Add a Flatten layer:
# • Use model.add() to add a Flatten layer. This layer flattens the 2D feature maps into a 1D vector,
# preparing the data for the dense layers.

from tensorflow.keras.layers import Flatten

model.add(Flatten())
model.summary()

# prompt: Add a Dense layer with 64 units:
# • Add a fully connected Dense layer with:
# o Units: 64.
# o Activation function: 'relu'.

from tensorflow.keras.layers import Dense

model.add(Dense(64, activation='relu'))
model.summary()

# prompt: Add an output Dense layer:
# • Add another Dense layer for the output with:
# • Units: 10 (corresponding to the 10 classes).
# • No activation function specified since it will be combined with a loss function that expects logits

model.add(Dense(10)) # Output layer with 10 units and no activation
model.summary()

# prompt: Compile the model:
# • Use the compile() method to configure the training process:
# • Optimizer: 'adam' (for adaptive gradient optimization).
# • Loss function: SparseCategoricalCrossentropy with from_logits=True (use logits for numerical
# stability).
# • Metrics: ['accuracy'].

from tensorflow.keras.losses import SparseCategoricalCrossentropy

model.compile(optimizer='adam',
              loss=SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# prompt: Train the model:
# • Use model.fit() to train the model with:
# • Training images and labels: train_images and train_labels.
# • Epochs: 10 (number of passes over the training dataset).
# • Validation data: (test_images, test_labels) to evaluate performance on the validation set.

history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels))