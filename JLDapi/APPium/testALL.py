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
                   # 'noReset': 'true',
                  "unicodeKeyboard": 'true',
                  "resetKeyboard": 'true',
                  "noSign": 'true',
                  "recreateChromeDriverSessions": 'true'
                }

globals()
dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
dr.implicitly_wait(5)

# 获得机器屏幕大小x,y
def getSize():
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    dr.swipe(x1, y1, x1, y2, t)


# 屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    dr.swipe(x1, y1, x1, y2, t)


# 屏幕向左滑动
def swipLeft(t):
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    dr.swipe(x1, y1, x2, y1, t)


# 屏幕向右滑动
def swipRight(t):
    l = getSize()
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    dr.swipe(x1, y1, x2, y1, t)


# 调用向左滑动
swipLeft(1000)
sleep(3)
# 调用向右滑动
swipRight(1000)
#调用向上滑动
swipeUp(1000)
#调用向下滑动
swipeDown(1000)