#coding:utf8
from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys

#启动浏览器\
mobileEmulation = {'deviceName': 'iPhone X'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

driver.get(u" http://101.fout.zyxr.com:2880/wapH5/#/register")
#登陆借立得
driver.find_element_by_xpath("//*[@id='root']/div/div/ul/li[1]/input").send_keys("13686805854")

t=driver.find_element_by_xpath("//*[@id='root']/div/div/ul/li[2]/div/span")
print(t)
t.send_keys(Keys.ENTER)
sleep(2)

driver.find_element_by_xpath("//*[@id='root']/div/div/ul/li[2]/input").send_keys("0000")
sleep(2)
d=driver.find_element_by_xpath("//*[@id='root']/div/div/ul/button")
sleep(2)
print(d)
d.send_keys(Keys.ENTER)

# driver.find_element_by_xpath("//*[@id='root']/div/form/div[3]/div/div/button").click()
#
# #进入用户管理
# # driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/ul/li[2]/div/span/span").click()
# sleep(2)
# #点击认证状态
# # a=driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/div/ul/li[1]/a").text
# # print(a)
# #错误用户名
# # b=driver.find_element_by_xpath("html/body/div[3]/div/span/div/div/div/span").text
# # print(b)
# #请输入用户名
# c=driver.find_element_by_xpath("html/body/div[1]/div/form/div[1]/div/div/div").text
# print(c)
# #退出
# driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[2]/div/span[2]").click()
# # sleep(3)
#
# driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/span[2]").click()
