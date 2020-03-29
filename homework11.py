# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:49:42 2020

@author: zongwen
"""
import numpy as np
import tensorflow as tf
x1=tf.constant([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
x2=tf.constant([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
y=tf.constant([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
x0=tf.ones(len(x1))
x2 = tf.cast(x2, dtype=tf.float32)
X=tf.stack((x0,x1,x2),axis=1)
Y=tf.reshape(y,(-1,1))
Xt=tf.transpose(X)  #计算X‘
XtX_1 = np.linalg.inv(tf.matmul(Xt,X))#计算(X'X)-1
XtX_1_Xt=tf.matmul(XtX_1,Xt)#计算(X'X)-1X'
W=tf.matmul(XtX_1_Xt,Y)#计算(X'X)-1X'Y

print("请输入房屋面积和房间数，预测房屋销售价格")
a = float(input("商品房面积："))
b = int(input("房间数："))

while a < 20 or a > 500 :
    print('输入有误，面积请输入20-500之间的实数')
    a = float(input("商品房面积："))
while type(b) is not int or b<1 or b>10:
    print('输入有误，房间数请输入1-10之间的整数')
    b = int(input("房间数："))    

y_pred=W[1]*a+W[2]*b+W[0]
d = np.asarray(y_pred)
print("预测价格：",round(d[0],2),"万元")
        


