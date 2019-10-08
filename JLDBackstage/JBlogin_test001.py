#coding=utf-8

from JLDBackstage import JBlogin
import unittest,csv

class jbTestCases01(unittest.TestCase):

    def setUp(self):
        print("-- testcase start --")
        global rzLogin,data
        self.baseUrl = u"http://192.168.9.101/admin/#/login"
        self.rzLogin = JBlogin.Login(self.baseUrl)
        self.succ = "PASS--"

        file = open("C:/Users/zy/Desktop/datatest.csv", "r")
        csvdata = csv.reader(file)
        data = [row for row in csvdata]



    def tearDown(self):
        print("-- testcase finished --")

    def CheckLogin(self):
        a=self.rzLogin.checkLogin()
        self.assertIn("桌面",a)
    def CheckPassName(self):
        b=self.rzLogin.checkPassName()
        self.assertIn("密码错误",b)
    def CheckUserName(self):
        c=self.rzLogin.checkUserName()
        self.assertIn("请输入用户名!",c)
    def CheckPass(self):
        d=self.rzLogin.checkPass()
        self.assertIn("你好",d)


    def test_log_in_01(self):
        print("-- testcase_01 正确的用户名密码 --")
        self.rzLogin.log_in(data[1][0], data[1][1])
        self.CheckLogin()
        self.rzLogin.logout()

    def test_log_in_02(self):
        print("-- testcase_02 错误的用户名密码 --")
        self.rzLogin.log_in(data[2][0], data[2][1])
        self.CheckPassName()
        self.rzLogin.closeDriver()


    def test_log_in_03(self):
        print("-- testcase_03 空的用户名 --")
        self.rzLogin.log_in(data[3][0], data[3][1])
        self.CheckUserName()
        self.rzLogin.closeDriver()

    def test_log_in_04(self):
        print("-- testcase_04 空的密码 --")
        self.rzLogin.log_in(data[4][0], data[4][1])
        self.CheckPass()
        self.rzLogin.closeDriver()


