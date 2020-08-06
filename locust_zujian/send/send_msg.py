#coding:utf-8

from locust import HttpLocust,TaskSet,task,between
from random import choice
import requests
import json
import os

class Message(TaskSet):

    def on_start(self):
        filepath = os.getcwd() + "\data.txt"
        with open(filepath, "rb") as file:
            self.data = file.read()

    @task()
    def send_message(self):


        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryUxGryjpPnr8AVzAR"
        }
        with self.client.post(url="/sdk/v2/message/send",data=self.data,headers=header,catch_response=True) as response:
            if "200" in response.text:
                response.success()
            else:
                response.failure("断言失败")
                print(response.text.encode('utf-8').decode('unicode_escape'))



class locust_User(HttpLocust):
    task_set = Message
    wait_time = between(1,1)
    host = "https://api.vhallyun.com"


if __name__ == '__main__':
    pypath = os.path.abspath(__file__)
    os.system("locust -f {} --no-web -c 1 -r 0".format(pypath))