#coding:utf-8

import threading
import datetime

class Demo(object):

    def __init__(self):
        pass

    def test_01(self,threadname):
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(threadname,now_time)
    def test_02(self,threadname):
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(threadname,now_time)

if __name__ == "__main__":
    demo = Demo()
    t1= threading.Thread(target=demo.test_01,args=("thread-01",))
    t2= threading.Thread(target=demo.test_02,args=("thread-02",))
    t1.start()
    t2.start()



