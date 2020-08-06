#coding:utf-8
'''
使用python第三方库requests 发送content_type类型为 multipart/form-data 的请求
'''
import requests
import json
#方法一
data = {
    "client": (None, "pc_browser"),
    "app_id": (None, "af314787"),
    "third_party_user_id": (None, "1611"),
    "access_token": (None, "access:af314787:7eaf668dc39ab733"),
    "package_check": (None, "package_check"),
    "type": (None, "service_im"),
    "channel_id": (None, "ch_365cd1f3"),
    "no_audit": (None, "0"),
    "body": (None, json.dumps({"type":"text","text_content":"1"})),
    "context": (None, json.dumps({"nickname":"tianqi","role_name":"1","replyMsg":{},"atList":[],"roleNameText":{"text":"主持人","type":"host"}}))
}
response = requests.post(url="https://api.vhallyun.com/sdk/v2/message/send",files=data)
print(response.json())

#方法二
# from requests_toolbelt import MultipartEncoder
# m = MultipartEncoder(fields={
#     "client":"pc_browser",
#     "app_id":"af314787",
#     "third_party_user_id":"1611",
#     "access_token":"access:af314787:7eaf668dc39ab733",
#     "package_check":"package_check",
#     "type":"service_im",
#     "channel_id":"ch_365cd1f3",
#     "no_audit":"0",
#     "body": (None, json.dumps({"type":"text","text_content":"1"})),
#     "context": (None, json.dumps({"nickname":"tianqi","role_name":"1","replyMsg":{},"atList":[],"roleNameText":{"text":"主持人","type":"host"}}))
# })
# header = {"Content-Type":m.content_type}
# response = requests.post(url="https://api.vhallyun.com/sdk/v2/message/send",data=m,headers=header)
# print(response.text.encode("utf-8").decode("unicode_escape"))

