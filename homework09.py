# -*- coding: utf-8 -*-
"""
@author: zongwen
"""

import tensorflow as tf

import numpy as np
x=tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y=tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

averx = tf.reduce_mean(x)
avery = tf.reduce_mean(y)
sum1=sum2=0
for n in x:
    sum1+=tf.square(n-averx)
for c,d in zip(x,y):
    sum2+=(c-averx)*(d-averx)
w=sum2/sum1
b=avery-w*averx

print("w=",w.numpy())  
print("b=",b.numpy()) 






