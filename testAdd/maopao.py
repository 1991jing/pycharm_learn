# coding=utf-8
import os
import requests
from bs4 import BeautifulSoup

# file='e:\\'
# for root,dirs,files in os.walk(file):
#     for file in dirs:
#         print(root + os.sep + file)


array = [2,5,9,4,1,6,3,8,7,0]
for i in range(len(array))[::-1]:
    for j in range(i):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array)

url = 'http://www.testclass.net/' # 定义被抓取页面的url
# 获取被抓取页面的html代码，并使用html.parser来实例化BeautifulSoup，属于固定套路
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# 遍历页面上所有的h4
for course in soup.find_all('h4'):
    # 打印出h4的text属性
    print(course.text)

print("hello , world")