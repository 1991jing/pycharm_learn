# -*- coding:utf-8 -*-
import requests
from JLDapi.publi.mysql_test import *
#登陆
url0="http://192.168.9.101/AdminWeb/login/login.json"
#费用列表
url = "http://192.168.9.101/AssetAdminWeb/productFee/getList.json"
#合同模板
url2="http://192.168.9.101/CMSAdminWeb/contract/getContractType.json"



payload="feeId=248100743308019&status=1"

headers = { "content-type": "application/json"}

sql ="SELECT a.`username`,a.`password` FROM admin.`t_admin` a WHERE realname='jing';"
SQL=mysql()
a=SQL.select_step(sql)
print(a[0][0])
print(a[0][1])


# login2= requests.request("POST",u"http://192.168.9.101/AdminWeb/login/login.json",
#                          data="username=zjw&password=356a192b7913b04c54574d18c28d46e6395428ab")
login = requests.post(url0,data={'username':a[0][0],'password':a[0][1]})
print(login.text)
print(login.url)
print(login.status_code)
cookie=login.cookies
print(cookie)

#cookies=login.cookies

response = requests.request("POST", url=url2, data="", cookies=login.cookies)

print(response.text)

print(response.status_code)

print(response.reason)
# print(response.raise_for_status())
# print(response.json())

import os,time
NowTime = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filename = os.path.join(os.getcwd(), "Report/result_" + NowTime + ".html")
print(filename)