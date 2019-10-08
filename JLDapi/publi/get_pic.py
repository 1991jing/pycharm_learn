#-*-coding:utf-8-*-
import requests

url = "http://192.168.9.101/admin/images/u10.e874f26c.png"
get_pic = requests.get(url,stream=True)

with open('pic1.jpg',"wb") as fd:
    for chunk in get_pic.iter_content(128):
        fd.write(chunk)

print(get_pic.status_code)
print(get_pic.reason)


