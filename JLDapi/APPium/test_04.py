# -*- coding: utf-8 -*-
__author__ = 'zy'
from appium import webdriver
from time import sleep
import csv
desired_caps = {
                  "platformName": "Android",
                  "platformVersion": "7.1",
                  "deviceName": "MiNote3",
                  "appPackage": "com.rttx.jielide",
                  "appActivity": "com.rttx.jielide.activity.MainActivity",
                  "udid": "917e90fd",
                    'noReset': 'true',
                  "unicodeKeyboard": 'true',
                  "resetKeyboard": 'true',
                  "noSign": 'true',
                  "recreateChromeDriverSessions": 'true'
                    }
driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub',
                               desired_capabilities=desired_caps)
sleep(5)
print("start")

file = open("D:/NewPython/JLDapi/APPium/element.csv", "r")
csvdata = csv.reader(file)
data = [row for row in csvdata]

# x = driver.get_window_size()['width']
# y = driver.get_window_size()['height']
# print(x,y)
# print()
# x1=int(x*0.75)
# y1=int(y*0.5)
# x2=int(x*0.05)
# print(x1,y1,x2)
# driver.swipe(x1,y1,x2,y1,1000)
# driver.swipe(x1,y1,x2,y1,1000)
# print("go")

# driver.find_element_by_xpath(data[13][1]).click()
driver.find_element_by_xpath(data[1][1]).click()
#切换账号
driver.find_element_by_xpath(data[2][1]).click()
driver.find_element_by_xpath(data[3][1]).send_keys("13686805854")
driver.find_element_by_xpath(data[4][1]).click()
# listElements = driver.find_elements_by_class_name("android.view.ViewGroup")
# listElements[5].click()
driver.find_element_by_xpath(data[5][1]).send_keys("ab123456")
driver.find_element_by_xpath(data[6][1]).click()
#X掉
driver.find_element_by_xpath(data[7][1]).click()
#点击头像
driver.find_element_by_xpath(data[8][1]).click()
driver.find_element_by_xpath(data[9][1]).click()
driver.find_element_by_xpath(data[10][1]).click()
sleep(2)
driver.find_element_by_xpath(data[11][1]).click()
sleep(1)
driver.quit()
print("__end__")


