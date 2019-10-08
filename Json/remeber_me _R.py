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
    filename = 'username.json'
    try:
        with open(filename) as  f_obs:
            username = json.load(f_obs)
    except FileNotFoundError:
        return None
    else:
        return username
"""问候用户，并指出名字"""
def greet_user():
    username = get_stored_name()
    if username:
        print("Welcome back ,"+username+"!")
    else:
        username=get_new_username()
        print("we will remeber you when you come back," + username + "!")


def get_new_username():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

greet_user()







