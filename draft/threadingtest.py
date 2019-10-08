# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     threadingtest
   Description :   testing
   Author :       zy
   date：          2018/8/6
-------------------------------------------------
   Change Activity: 2018/8/6:
-------------------------------------------------
"""
__author__ = 'zy'

import threading
import time

def run(n):
    print("task-%s" % n)
    time.sleep(5)

#实例化一个线程对象，target传入任务名，args以元组的形式传入任务函数的参数
task1 = threading.Thread(target=run, args=(1,))
task2 = threading.Thread(target=run, args=(2,))

task1.start()   #线程启动
task2.start()