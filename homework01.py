# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
利用Python完成一元二次方程的求解，要求程序输入任意的值后，
程序能判断输出有解或无解，有解的话，输出的解为多少。
"""

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

test = b*b-4*a*c
if a == 0:
    print("a不能为0，不是一元二次方程")
elif test >= 0:
    print("该方程有两个解。")
    x1 = (-b + test ** 0.5)/(2*a)
    x2 = (-b - test ** 0.5)/(2*a)
    if x1 != x2:
        print("方程的两个根分别是：x1 = %f,x2 = %f"%(x1,x2))
    else:
        print("方程的根为：x = %f"%(x1))
else:
    print("该方程无解。")