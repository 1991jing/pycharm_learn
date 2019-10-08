# -*- coding: UTF-8 -*-

# from tkinter import *  # 导入 Tkinter 库
#
# root = Tk()  # 创建窗口对象的背景色
# # 创建两个列表
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(root)  # 创建两个列表组件
# listb2 = Listbox(root)
# for item in li:  # 第一个小部件插入数据
#     listb.insert(0, item)
#
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
#
# listb.pack()  # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()  # 进入消息循环


# import random
#
# print( random.randint(1,3) )        # 产生 1 到 3 的一个整数型随机数
# print( random.randint(1,3) )
# print( random.randint(1,3) )
# print( random.randint(1,3) )
# print( random.randint(1,3) )
# print( random.randint(1,3) )
#
# import random
#
# mobile=random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(10))
# print(mobile)


# import requests
# from sys import argv
#
# USAGE = '''
# USAGE:
# python get.py https://api.github.com
# '''
#
# if len(argv) != 2:
#   print(USAGE)
#   exit()
#
# script_name, url = argv
#
# if url[:4] != 'http':
#   url = 'http://' + url
#
# r = requests.get(url)
#
# print(u"接口地址: {url}\n")
# print(u"状态码: {r.status_code}\n")
# print(u"Headers:")
# for key, value in r.headers.items():
#   print(u"{key} : {value}")
#
# print(r.text)


