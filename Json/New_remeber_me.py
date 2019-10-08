# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     remeber_me _R
   Description :   testing
   Author :       zy
   date：          2018/6/23
-------------------------------------------------
   Change Activity: 2018/6/23:
-------------------------------------------------
"""
__author__ = 'zy'

import  json

"""如果存储了姓名，就获取它"""
def get_stored_name():
    filename = 'get_username'
    try:
        with open(filename) as  f_obs:
            username = f_obs.read()
    except FileNotFoundError:
        return ""
    else:
        return username

def get_new_username():
    nusername = input("What is your name?")
    yusername = get_stored_name()
    filename = 'get_username'
    if nusername in yusername:
        return nusername
    else:
        with open(filename,'a') as f_obj:
           json.dump(nusername,f_obj)
        return nusername

"""问候用户，并指出名字"""
def greet_user():
    times = int(input("How much times do you want to try?"))
    i = 0
    while times > i:
        username = get_stored_name()
        username2 = get_new_username()
        if username2 in username:
            print("Welcome back ," + username2 + "!")
        else:
            print("we will remeber you when you come back," + username2 + "!")
        filename = 'get_username'
        with open(filename) as f_obj:
            updata=f_obj.read()
        print("The database has been updated:" + updata)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        i+=1
    else:
        print("Maximum output number")

greet_user()






