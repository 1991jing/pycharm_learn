# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     jsonTest
   Description :   testing
   Author :       zy
   date：          2018/6/22
-------------------------------------------------
   Change Activity: 2018/6/22:
-------------------------------------------------
"""
__author__ = 'zy'
import json
print (json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=10, separators=(',,,', ':: ')))




s= "A:1|B:2|C:3|D:4".split('|')
print(s)
d= dict()
print(d)
for temp in s:
    # print(temp[0]), print(temp[1]), print(temp[2])
   d[temp[0]] = temp[2]
print(str(d))

json.loads(str(d).replace('\'', "\""))


print("=============")

s1={"c":3,"b":1,"a":2}
print(type(s1))
#s1 =json.dumps(s1,sort_keys=True)
s = sorted(s1.items(),key=lambda s1:s1[1])

print(type(s))
print(s)




print("=============>>")

item =sorted(s1.values())
s2={}
print(item)
item2 =sorted(s1.keys())
print(item2)
for i in item2:
    s2[i]=s1[i]
print(s2)
print(type(s2))

dict1={'a':2,'e':3,'f':8,'d':4}
list1= sorted(dict1.items(),key=lambda x:x[1])
print(list1)