# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_interface
   Description :   testing
   Author :       zy
   date：          2018/3/6
-------------------------------------------------
   Change Activity: 2018/3/6:
-------------------------------------------------
"""
__author__ = 'zy'



import requests

url = "http://94.fout.zyxr.com:2880/BusinessOpenWeb/sign/signWithHold.json"

payload ={"appid": "d5a3522f88291621f4e915abae719c34",
            "currentTime": 1503538749619,
            "data": "{\"openid\":\"2c94558cce5290d441b311f156a24b3e2615476e\"}",
            "checksum": "e4819efbf1626e51489b2dfa70900ab9"
        }



#headers ={'Content-Type':'applocation/json;charset=utr-8'}
response = requests.post( url, data=payload)

print(response.text)