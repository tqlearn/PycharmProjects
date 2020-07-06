#coding :utf-8
import requests
from operation.read_json import ReadExcel
class  SendMessage(object):

    def __init__(self,url,data):
        self.data = self.request_send(url,data)

    def request_send(self,url,data):
        res = requests.post(url,data)
        return res

if __name__ == "__main__":
    url = 'https://api.vhallyun.com/sdk/v2/message/send'
    filename = '..\config\data.json'
    data = ReadExcel(filename).data


    sum = 0
    for i in range(0,10):
        send = SendMessage(url, data).data
        print(send.json())
        sum =sum + 1
    print(sum)

