# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     paramtest
   Description :   testing
   Author :       zy
   date：          2018/8/3
-------------------------------------------------
   Change Activity: 2018/8/3:
-------------------------------------------------
"""
__author__ = 'zy'
import unittest
import paramunittest
import time
# python3.6
# 作者：上海-悠悠

@paramunittest.parametrized(
    {"user": "admin", "psw": "123", "result": "true"},
    {"user": "admin1", "psw": "1234", "result": "true"},
    {"user": "admin2", "psw": "1234", "result": "true"},
    {"user": "admin3", "psw": "1234", "result": "true"},
    {"user": "admin4", "psw": "1234", "result": "true"},
    {"user": "admin5", "psw": "1234", "result": "true"},
    {"user": "admin6", "psw": "1234", "result": "true"},
    {"user": "admin7", "psw": "1234", "result": "true"},
    {"user": "admin8", "psw": "1234", "result": "true"},
    {"user": "admin9", "psw": "1234", "result": "true"},
    {"user": "admin10", "psw": "1234", "result": "true"},
    {"user": "admin11", "psw": "1234", "result": "true"},
)

class TestDemo(unittest.TestCase):
    def setParameters(self, user, psw, result):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.user = user
        self.psw = psw
        self.result = result

    def testcase(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.psw)
        print("期望结果：%s " % self.result)
        time.sleep(0.5)
        self.assertTrue(self.result == "true")


if __name__ == "__main__":
    unittest.main(verbosity=2)