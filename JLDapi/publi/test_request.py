#coding:utf-8
import requests ,json

url = "http://101.fout.zyxr.com:2880/jld-mobile-wap/user/isRegister.json"

payload = "{\"data\":\"{\\\"userName\\\":\\\"13686805852\\\",\\\"ostype\\\":\\\"4\\\",\\\"channel\\\":\\\"aaa\\\",\\\"imsi\\\":\\\"\\\",\\\"latitudeLongitude\\\":\\\"\\\",\\\"network\\\":\\\"3g\\\",\\\"phoneResolution\\\":\\\"1080x1794\\\",\\\"rnVersion\\\":\\\"\\\",\\\"phoneType\\\":\\\"google\\\",\\\"systemVersion\\\":\\\"24\\\",\\\"version\\\":\\\"1.0.5\\\"}\",\"checksum\":\"\",\"currentTime\":1526971402128}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "7e5aa7be-ab8b-a0a1-dde9-7dfdeb0b399d"
    }

response = requests.request("POST", url, data=payload, headers=headers)

filname="request_text.json"
with open (filname,"w")as f:
    json.dump(response.text,f)

jsonrrsponse = response.json()
print(response.text)

print(jsonrrsponse)