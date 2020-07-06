#coding:utf-8

import os
import sys

#获取当前工程路径
print(os.getcwd())
sys.path.append(os.getcwd())
print(sys.path)



r'C:\Users\tianqi\PycharmProjects\卫材'



# ['C:\\Users\\tianqi\\PycharmProjects\\卫材',
#  'C:\\Users\\tianqi\\PycharmProjects\\卫材',
#  'C:\\Users\\tianqi\\PycharmProjects\\卫材\\demo',
#  'C:\\Users\\tianqi\\PycharmProjects\\卫材\\operation',
#  'D:\\Program Files\\Python\\Python37\\python37.zip',
#  'D:\\Program Files\\Python\\Python37\\DLLs',
#  'D:\\Program Files\\Python\\Python37\\lib',
#  'D:\\Program Files\\Python\\Python37',
#  'C:\\Users\\tianqi\\AppData\\Roaming\\Python\\Python37\\site-packages',
#  'D:\\Program Files\\Python\\Python37\\lib\\site-packages',
#  'C:\\Users\\tianqi\\PycharmProjects\\卫材']



'''
raise 指程序在执行过程中，发生了用户输入的数据与要求数据不符、用户操作错误等问题，
        这些问题都需要程序进行处理并给出相应的提示。
'''
#用户登录判断
try:
    print("请输入用户名")
    username = input(">")
    if username != "tianqi":
        raise Exception("用户名错误")   #主动抛出EXception异常
except Exception as err:    #匹配异常类型，匹配成功执行并输出err
    print(err)


# print("请输入用户名")
# username = input(">")
# if username != "tianqi":
#     raise Exception("用户名错误")   #raise异常抛出后，后面的代码不执行

# try:
#     a
# except Exception as err:
#     raise Exception("a 报错了",err)
#     # print("a 报错了",err)

try:
    a
    raise Exception("a没有被定义")
except Exception as err:
    print("a 报错了==========>",err)