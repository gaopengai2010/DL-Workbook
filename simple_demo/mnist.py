# -*- coding: utf-8 -*-
"""mnist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MAB0cLd4OpeS7wX7cjh4fowtaYd-tD9T
"""

import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train, y_train

print(x_train.size, y_train.size, x_test.size, y_test.size)

x_train.shape, y_train.shape, x_test.shape, y_test.shape

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

"""使用 Model.fit 方法调整您的模型参数并最小化损失："""

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

"""现在，这个照片分类器的准确度已经达到 98%。想要了解更多，请阅读 TensorFlow 教程。

如果您想让模型返回概率，可以封装经过训练的模型，并将 softmax 附加到该模型：
"""

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

probability_model(x_test[:5])