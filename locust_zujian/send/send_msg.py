#coding:utf-8

from locust import HttpLocust,TaskSet,task,between
from random import choice
import requests
import json
import os
import queue

class Message(TaskSet):

    def on_start(self):
        pass

    @task()
    def send_message(self):
        value = self.locust.queuevalue.get_nowait()
        data = {
            "client": (None, "pc_browser"),
            "app_id": (None, "af314787"),
            "third_party_user_id": (None, "1611"),
            "access_token": (None, "access:af314787:7eaf668dc39ab733"),
            "package_check": (None, "package_check"),
            "type": (None, "service_im"),
            "channel_id": (None, "ch_365cd1f3"),
            "no_audit": (None, "0"),
            "body": (None, json.dumps({'type':'text','text_content':value})),
            "context": (None, json.dumps({'nickname':'tianqi','role_name':'1','replyMsg':{},'atList':[],'roleNameText':{'text':'主持人','type':'host'}}))
        }

        with self.client.post(url="/sdk/v2/message/send",files=data,catch_response=True) as response:
            if "200" in response.text:
                response.success()
            else:
                response.failure("断言失败")
                print(response.text.encode('utf-8').decode('unicode_escape'))



class locust_User(HttpLocust):
    task_set = Message
    wait_time = between(1,1)
    host = "https://api.vhallyun.com"

    queuevalue = queue.Queue()
    for i in range(1,201):
        queuevalue.put_nowait("第 " + str(i) + " 条消息")


if __name__ == '__main__':
    pypath = os.path.abspath(__file__)
    os.system("locust -f {} --no-web -c 1 -r 0".format(pypath))