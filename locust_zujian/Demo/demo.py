#coding:utf-8

import os

path = os.getcwd()
print(os.path.dirname(path) + "\\"+"Parametric\\"+"data.csv")
print(os.path.join(os.path.dirname(path),"Parametric\\"))