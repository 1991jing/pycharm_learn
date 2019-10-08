# coding=utf-8
from time import sleep
from selenium import webdriver

#封装登录页面功能类
class Login(object):

    def __init__(self, url):
        self.base_url = url
    #析造函数
    def __del__(self):
        pass
    #打开浏览器
    def openDriver(self):

        self.driver = webdriver.Firefox()#打开火狐
        self.driver.maximize_window()#最大化窗口

        self.driver.implicitly_wait(1)
        return self.driver
    #关闭浏览器
    def closeDriver(self):
        try:
            self.driver.close()
            return True
        except Exception as e:
            print("浏览器对象不存在！")
            return False

    #username：登录用户名
    #password：登录的密码
    def log_in(self, username, password, url=""):
        self.openDriver()                   #打开一个空白的火狐浏览器
        if url == "":                       #如果url没有传进来
            url = self.base_url             #则使用实例化的时候传进来的URL
        self.driver.get(url)                #打开url登录首页

        try:
            self.driver.find_element_by_id("userName").send_keys(username)#定位到用户名字段并输入用户名
            self.driver.find_element_by_id("password").send_keys(password)#定位到密码字段并输入密码
            self.driver.find_element_by_xpath("//*[@id='root']/div/form/div[3]/div/div/button").click()
            sleep(1)

        except Exception as e:
            print("ERR  --  测试用例执行失败，信息：%s"%e)
        return self.driver

    def checkLogin(self):
        logtext=self.driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/div/ul/li[1]/a").text
        return logtext
    def checkPassName(self):
        errPass=self.driver.find_element_by_xpath("html/body/div[3]/div/span/div/div/div/span").text
        return errPass
    def checkUserName(self):
        errName=self.driver.find_element_by_xpath("html/body/div[1]/div/form/div[1]/div/div/div").text
        return errName
    def checkPass(self):
        errPass=self.driver.find_element_by_xpath("html/body/div[1]/div/form/div[2]/div/div/div").text
        return errPass

    def logout(self):
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[2]/div/span[2]").click()
        self.driver.quit()





