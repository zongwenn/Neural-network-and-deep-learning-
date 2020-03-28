# -*- coding: utf-8 -*-
"""
@author: zongwen
"""

import tensorflow as tf
x=tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y=tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

sumx = tf.reduce_sum(x)
sumy = tf.reduce_sum(y)
a=tf.multiply(x,y)
sumxy = tf.reduce_sum(a)  
squaresumx = tf.reduce_sum(tf.square(x))
sumsquarex = tf.square(tf.reduce_sum(x))
w = (10*sumxy - sumx*sumy)/(10*squaresumx-sumsquarex)
b = (sumy-w.numpy()*sumx)/10
print("w=",w.numpy())  
print("b=",b.numpy()) 


