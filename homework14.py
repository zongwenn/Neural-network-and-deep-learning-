# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 22:14:46 2020

@author: zongwen
"""
import tensorflow.compat.v1 as tf
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
tf.disable_eager_execution()    #防止抛出异常

class Train:
    def __init__(self,route):
        self.df = pd.read_csv(route,header = 0)  #读取csv文件
        print(self.df.describe())        #显示数据摘要信息
        self.df = self.df.values        #获取df的值
        self.df = np.array(self.df)           #把self.df转换为np数组的形式
        
    def Standard(self):
        for i in range(12):
            self.df[:,i] = (self.df[:,i] - self.df[:,i].min())/(self.df[:,i].max() - self.df[:,i].min())
        self.x_data = self.df[:,:12]     #self.x_data为前12列的特征数据
        self.y_data = self.df[:,12]     #self.y_data为最后一列的标签数据
       
    def model(x,w,b):      #矩阵相乘,w和x
        return tf.matmul(x,w) + b
    
    def Matrix(self):
        #定义特征数据和标签数据的占位符
        self.x = tf.placeholder(tf.float32,[None,12],name="X")  #12个特征数据，12列，None表示行数未知
        self.y = tf.placeholder(tf.float32,[None,1],name="Y") #1个标签数据，1列
        #定义一个命名空间
        with tf.name_scope("Model"):
            #初始化值为shape=(12,1)的随机数，标准差为0.01     
            self.w = tf.Variable(tf.random_normal([12,1],stddev = 0.01),name = "W")
            self.b = tf.Variable(1.0,name = "b")      #b的初始值为1.0
            self.pred = Train.model(self.x,self.w,self.b)  #预测计算操作，前向计算节点
            
    def LossFunction(self,train_epochs,learning_rate):
        self.train_epochs,self.learning_rate = train_epochs,learning_rate
        
        with tf.name_scope("LossFunction"):     #定义均方差损失函数
            self.loss_function = tf.reduce_mean(tf.pow(self.y - self.pred,2))     #均方误差
        #创建梯度下降优化器
        self.optimizer = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.loss_function)
        self.sess =tf.Session()   #声明会话
        self.init = tf.global_variables_initializer()    #定义初始化变量的操作
        self.sess.run(self.init)       #启动会话


            
    def iteration(self):
        
        self.loss_list = []   #初始化空列表，用于记录每轮训练后的损失值
        #进行迭代训练
        for epoch in range(self.train_epochs):
            self.loss_sum = 0.0  #每轮损失函数的总和
            for xs,ys in zip(self.x_data,self.y_data):
                xs = xs.reshape(1,12)    #重塑维度
                ys = ys.reshape(1,1)
                
                _,self.loss = self.sess.run([self.optimizer,self.loss_function],feed_dict={self.x:xs,self.y:ys})
                self.loss_sum = self.loss_sum + self.loss
                
            #打乱数据顺序
            self.x_data,self.y_data = shuffle(self.x_data,self.y_data)

            self.b0temp = self.b.eval(session = self.sess)
            self.w0temp = self.w.eval(session = self.sess)

            self.loss_average = self.loss_sum/len(self.y_data)    #平均损失率
            self.loss_list.append(self.loss_average)     #每轮添加一次

            #打印每轮训练的信息
            print("epoch={0:<5}loss={1:<15.7f}b={2:<15.7f}".format(epoch+1,self.loss_average,self.b0temp))
            print("w=")
            print(self.w0temp)
        
        print("\n")
        print("每次训练的平均损失值为：")   
        print(self.loss_list)
        
        
    def test(self):
        for i in range(3):
            self.n = np.random.randint(506)
            print("\n")
            print("您当前随机抽取的是第{}条数据".format(self.n))
            self.x_test = self.x_data[self.n]

            self.x_test = self.x_test.reshape(1,12)
            self.predict = self.sess.run(self.pred,feed_dict={self.x:self.x_test})
            print("预测值：%f"% self.predict)
            self.target = self.y_data[self.n]
            print("标签值：%f"% self.target)

        
    
route = r"C:\Users\zongwen\Desktop\神经网络与深度学习\boston.csv"  
train_epochs = eval(input("请输入您要进行迭代的次数："))        #迭代次数
learning_rate = float(input("请输入你要调整的学习率："))    #学习率
T = Train(route)        #创建类Train对象T
T.Standard()           #对特征数据进行归一化
T.Matrix()            #模型定义与定义模型函数
T.LossFunction(train_epochs,learning_rate)     #定义损失函数
T.iteration()       #进行迭代训练
T.test()           #随机确定三条数据测试效果