#coding:utf-8

import threading
import unittest
import os
def run_test():

    discover = unittest.defaultTestLoader.discover(start_dir=os.getcwd(),pattern="demo_test*.py")
    return discover

if __name__ == '__main__':
    t=threading.Thread(target=run_test(),args=())
    t.start()
    rt = run_test()
    unittest.TextTestRunner().run(rt)

