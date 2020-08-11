#coding:utf-8
import sys
import requests
import os
def send_message():


    filepath = os.getcwd()+"\data.txt"
    with open(filepath,"rb") as file:
        data = file.read()
        print(data)

    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryUxGryjpPnr8AVzAR"
    }

    with requests.post(url="https://api.vhallyun.com/sdk/v2/message/send",data=data,headers=header) as response:
        if "200" in response.text:
            print("成功")
            print(response.text.encode("utf-8").decode("unicode_escape"))
        else:
            print("断言失败")
            print(response.text.encode("utf-8").decode('unicode_escape'))

if __name__ == '__main__':
    send_message()

