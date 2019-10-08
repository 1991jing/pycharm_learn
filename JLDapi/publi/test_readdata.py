# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_readdata
   Description :   testing
   Author :       zy
   date：          2018/2/9
-------------------------------------------------
   Change Activity: 2018/2/9:
-------------------------------------------------
"""
__author__ = 'zy'
import csv
file= open("C:/Users/zy/Desktop/datatest.csv","r")
csvdata=csv.reader(file)
data=[row for row in csvdata]
print(data)

for i in data :
    print(i[0])
    print(i[1])
