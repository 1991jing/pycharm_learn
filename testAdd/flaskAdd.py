# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     flaskAdd
   Description :   testing
   Author :       zy
   date：          2018/2/11
-------------------------------------------------
   Change Activity: 2018/2/11:
-------------------------------------------------
"""
__author__ = 'zy'


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world! Forget it!"


def simple_decorator(f):
    def wrapper():
        print ("func enter")
        f()
        print("func exit")

    return wrapper


@simple_decorator
def hello():
    print("Hello World!")


hello()
# if __name__ == '__main__':
#     app.run()