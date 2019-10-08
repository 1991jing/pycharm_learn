#coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] ='5fc7ac84'                #'Android Emulator'  '96d70849'
desired_caps['appPackage'] = 'com.rttx.jielide'
desired_caps['appActivity'] = '.activity.GuideActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver.find_element_by_id("com.rttx.jielide:id/ec").click()

#driver.find_element_by_class_name("android.widget.EditText").clear()

driver.find_element_by_class_name("android.widget.EditText").send_keys("13686805854")

driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'6')]").send_keys("ab123456")

driver.find_element_by_xpath("//android.view.ViewGroup[contains(@index,'10')]").click()

driver.find_element_by_id("com.rttx.jielide:id/ec").click()

driver.find_element_by_id("com.rttx.jielide:id/eb").click()

driver.find_element_by_name("退出登录").click()


sleep(3)

listElements = driver.find_elements_by_class_name("android.view.ViewGroup")

for a  in listElements:
    print(a)


listElements[8].click()

driver.find_element_by_id("com.rttx.jielide:id/fk").click()
sleep(2)
driver.find_element_by_id("com.rttx.jielide:id/li").click()
#点击立即借款
driver.find_element_by_id("com.rttx.jielide:id/hj").click()
#返回登录页面，点击忘记密码
driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'忘记密码?')]").click()

listElements2=driver.find_elements_by_class_name("android.view.ViewGroup")

for b in listElements2:
    b.click()


Text=driver.find_elements_by_class_name("android.widget.TextView")
for c in Text:
    print(c.text)

#driver.quit()

# driver.find_element_by_xpath("//android.view.ViewGroup[contains(@index,'2')]").click()

# driver.switch_to.alert.accept()
