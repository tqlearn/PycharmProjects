#coding:utf-8

import os
import requests
from urllib import parse

filename = os.path.dirname(__file__) + "/doctment.docx"

url = "https://t-open.e.vhall.com/api/v2/document/create"
data = {
    "app_id":"88a781ea",
    "signed_at":"1585649889",
    "sign":"vhall",
}
header ={
    "Content-Type":"application/x-www-form-urlencoded"
}

file = {'document': open(filename,"rb")}
res = requests.post(url=url,data=data,headers=None,files=file)
print(res.json())


'''
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None
'''
