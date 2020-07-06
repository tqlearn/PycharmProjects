#coding:utf-8
import os
import json
#                       获取当前文件所在的路径
jsonfile = os.path.join(os.path.dirname(__file__),'dict.json')
# data ={"aaa":"111"}
# with open(jsonfile,'w') as fp:
#     fp.write(json.dumps(data))

with open(jsonfile,'r') as fp:
    data = json.load(fp)   #读出来就是json
    # data = fp.read()  #读出来就是str
    print(data)
    print(type(data))



#获取路径
print(os.getcwd())
print(os.path.dirname(os.getcwd()))
#文件的绝对路径
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))