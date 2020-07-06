#coding:utf-8
'''
通过继承threading.Thread,并重写run()方法,来实现多线程
'''
import threading
import time

class MyThread(threading.Thread):
    """
    使用继承的方式实现多线程
    """
    def __init__(self, who):
        super().__init__()    # 必须调用父类的构造方法
        self.name = who

    def run(self):
        print("%s is run..." % self.name)
        time.sleep(3)

if __name__ == "__main__":
    t1 = MyThread("Jet")    # 创建线程1
    t2 = MyThread("Jack")   # 创建线程2
    t1.start()              # 运行线程1
    t2.start()              # 运行线程2
    print("\n over...")