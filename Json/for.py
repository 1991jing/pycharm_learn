# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     for
   Description :   testing
   Author :       zy
   date：          2018/6/26
-------------------------------------------------
   Change Activity: 2018/6/26:
-------------------------------------------------
"""
__author__ = 'zy'

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")


y=numbers_to_strings(3)
print(y)
# for num,lable in enumerate(lableList):
#         createVar['l'+str(num)]= []
#     for item in totalData:
#         itemLable = item.get(lableLevel)
#         for num in range(0,len(lableList)):
#             if itemLable==lableList[num]:
#                 locals()['l'+str(num)].append(item)
#                 break

# for i in range(1,3):
#     print(i)

# def test():
#     res=None
#     for i in range(1,3):
#         res=1+i
#         return res
#
#
# print(test())
# a=1
# b="2"
#
# print(isinstance(a,b))
'''做个简单的题目：从一个长度n的数组中找出最大的k个数，编码实现一下，至少两种方法，并比较各种方法的优劣。
例，当 n=5，k=3 时，输入 list = [1, 99, 88, 5, 4] ，输出 [99, 88, 5]'''
def bubble_sort(blist,k):
 n=len(blist)
 newlist=[]
 for i in range(0,n-1):
  for j in range(i+1,n):
   if blist[i]<blist[j]:
    blist[i],blist[j]=blist[j],blist[i]
 for z in range(0,k):
  newlist.append(blist[z])
 return newlist
blist=bubble_sort([32,12,45,64,1,5,8],3)
print(blist)