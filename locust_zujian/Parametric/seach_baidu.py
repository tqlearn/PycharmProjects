#coding:utf-8

from locust import HttpLocust,task,TaskSet,between
import os
import random
class SeachBaidu(TaskSet):
    def on_start(self):
        pass
    @task
    def seach(self):

        data = random.choice(self.locust.list)
        response = self.client.get(url="/s?wd={}".format(data))
        # print(response.text.encode("utf-8").decode("unicode_escape"))
        print(data)

class LocustUser(HttpLocust):
    task_set = SeachBaidu
    wait_time = between(1,1)
    host = "https://www.baidu.com"

    list = []
    csvpath = os.getcwd()+"\data.csv"
    with open(csvpath,"rb") as file:
        for i in file.readlines():
            list.append(i)
