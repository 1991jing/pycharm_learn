# -*- coding: utf-8 -*-
__author__ = 'zy'
from appium import webdriver
from time import sleep

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

globals()
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
print("start")

# def getSize():
#     x = driver.get_window_size()['width']
#     y = driver.get_window_size()['height']
#     return (x, y)
#
# def swipLeft(t):
#     l=getSize()
#     x1=int(l[0]*0.75)
#     y1=int(l[1]*0.5)
#     x2=int(l[0]*0.05)
#     driver.swipe(x1,y1,x2,y1,t)
#
# print("go")
# swipLeft(1000)



driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                             "android.widget.FrameLayout/android.widget.LinearLayout"
                             "/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"
                             "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                             "/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView"
                             "/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]"
                             "/android.widget.TextView").click()

driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                             "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                             "/android.view.ViewGroup[2]/android.widget.TextView").click()


driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                             "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                             "/android.view.ViewGroup/android.widget.EditText").send_keys("13686805854")


driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                             "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                             "/android.view.ViewGroup[4]").click()
# listElements = driver.find_elements_by_class_name("android.view.ViewGroup")
# listElements[5].click()



driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                             "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView"
                             "/android.view.ViewGroup/android.widget.EditText").send_keys("ab123456")

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                             "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView"
                             "/android.view.ViewGroup/android.view.ViewGroup[5]").click()
#X掉
driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                             "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]").click()

#点击头像
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                             "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                             "/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup"
                             "/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView").click()


driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                             "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView"
                             "/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView").click()


driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                             "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                             "/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView"
                             "/android.view.ViewGroup/android.view.ViewGroup[4]").click()
sleep(2)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                             "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                             "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
                             "/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[4]").click()

sleep(1)
driver.quit()
print("__end__")






