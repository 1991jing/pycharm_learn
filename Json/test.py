# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :   testing
   Author :       zy
   date：          2018/6/23
-------------------------------------------------
   Change Activity: 2018/6/23:
-------------------------------------------------
"""
__author__ = 'zy'

import json
'''写一个存储姓名的判断，已存有姓名则输入 您好+name,没有存有姓名则输出 已保存+name'''

i=1
while i<4:
    name=input("what is your name?")
    wj='name'
    with open(wj) as fg:
        ycdata=fg.read()

    if name in ycdata:
        print("hello "+name+"!"+",you are sign in.")
    else:
        with open(wj,'a') as fg:
            json.dump(name,fg)
            print("we will remeber you when you come back," + name + "!")

    with open(wj) as fg:
        ycdata=fg.read()
    print("The database has been updated:"+ycdata)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    i+=1

else:
    print("Maximum output number")















