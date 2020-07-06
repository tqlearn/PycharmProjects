#1、获取Cookie
#2、写入Cookie
#3、是否携带
import sys
import os
base_path=os.getcwd()
sys.path.append(base_path)
from Utils.handle_json import read_json,write_value
'''
data={
    "app":{
        'aaa':'bbbbbb'
    }
}    
'''
def get_cookie_value(cookie_key):
    '''
    获取cookie
    '''
    data=read_json("/config/Cookie.json")
    return data[cookie_key]

def write_cookie(data,cookie_key):
    '''
    写入cookie
    '''
    data1=read_json("/config/Cookie.json")
    data1[cookie_key]=data
    write_value(data1)

if __name__ == '__main__':
    # data={
    #     'aaaa':'123456'
    # }
    # write_cookie(data=data,cookie_key='web')
    a=get_cookie_value(cookie_key="web")
    print(type(a))
