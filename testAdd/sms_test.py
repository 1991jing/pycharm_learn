# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sms_test
   Description :   testing
   Author :       zy
   date：          2018/4/16
-------------------------------------------------
   Change Activity: 2018/4/16:
-------------------------------------------------
"""
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='===')
    print()




for i in range(1,10):
    for j in range(1,1+i):
        print("%dx%d=%d  "%(j,i,j*i),end='')
    print()