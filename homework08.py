# -*- coding: utf-8 -*-
"""
@author: zongwen
"""
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
mnist = tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y) = mnist.load_data()

plt.figure(figsize=(6,6))

for i in range(16):
    num = np.random.randint(1,50000)
    plt.subplot(4,4,(i+1))
    plt.axis("off")
    plt.imshow(train_x[num],cmap='gray')
    plt.title(train_y[num],fontsize=14)

plt.tight_layout()
plt.suptitle("MNIST测试集样本",x=0.5,y=1.1,color="red",fontsize=20)
plt.show()
