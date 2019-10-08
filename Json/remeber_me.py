# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     remeber_me
   Description :   testing
   Author :       zy
   date：          2018/6/23
-------------------------------------------------
   Change Activity: 2018/6/23:
-------------------------------------------------
"""
__author__ = 'zy'

import json

filename = 'username.json'
try:
    with open(filename) as f_obs:
        username = json.load(f_obs)
except FileNotFoundError:
    username = input("what is your name?")
    with open(filename,'w') as f_obs:
        json.dump(username,f_obs)
        print("we will remeber you when you come back,"+username+"!")
else:
    print("welcome back,"+username+"!")






