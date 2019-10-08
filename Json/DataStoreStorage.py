# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     DataStoreStorage
   Description :   testing
   Author :       zy
   date：          2018/6/23
-------------------------------------------------
   Change Activity: 2018/6/23:
-------------------------------------------------
"""
__author__ = 'zy'

import json

number=[2.35,2,82,9,6,'jack']
filename = 'number.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)

with open(filename) as f_obj:
    number = json.load(f_obj)

print(number)

for i in number:
    print(i)

