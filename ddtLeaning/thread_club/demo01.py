#coding:utf-8

'''
每个CPU在同一时间只能执行一个线程
（在单核CPU下的多线程其实都只是并发，不是并行，并发和并行从宏观上来讲都是同时处理多路请求的概念。
但并发和并行又有区别，并行是指两个或者多个事件在同一时刻发生；而并发是指两个或多个事件在同一时间间隔内发生。）


直接实例化threading.Thread线程对象,实现多线程
'''
import threading
import time

def print_age(who, age):
    """
    需要用多线程调用的函数
    :param who:
    :param age:
    :return:
    """
    print("Hello,every one!")
    time.sleep(1)
    print("%s is %s years old !" % (who, age))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_age, args=("jet", 18, ))     # 创建线程1
    t2 = threading.Thread(target=print_age, args=("jack", 25, ))    # 创建线程2
    t3 = threading.Thread(target=print_age, args=("jack", 25,))     # 创建线程3
    t1.start()    # 运行线程1
    t2.start()    # 运行线程2
    t3.start()    # 运行线程3
    print("over...")