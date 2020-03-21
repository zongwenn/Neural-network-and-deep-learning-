# -*- coding: utf-8 -*-
"""
@author: zongwen
"""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing

(train_x,train_y),(_,_) = boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("Traing set:",len(train_x))

titles = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B-1000","LSTAT","MEDV"]

print("1 -- CRIM")
print("2 -- ZN")
print("3 -- INDUS")
print("4 -- CHAS")
print("5 -- NOX")
print("6 -- RM")
print("7 -- AGE")
print("8 -- DIS")
print("9 -- RAD")
print("10 -- TAX")
print("11 -- PTRATIO")
print("12 -- B")
print("13 -- LSTAT")
a = int(input("请选择属性："))

plt.figure(figsize=(5,5))
plt.subplot(1,1,1)
plt.scatter(train_x[:,a-1],train_y)
plt.xlabel(titles[a])
plt.ylabel("Price($1000's)")
plt.title(str(a)+"."+titles[a-1]+" - Price")

plt.show()

#plt.tight_layout()
#plt.suptitle("各个属性与房价的关系",x=0.5,y=1.02,fontsize=20)






