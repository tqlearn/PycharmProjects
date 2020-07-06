import requests
import json
import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)
from Utils.handle_init import handle_ini
from Utils.handle_json import get_value
from Utils.handle_cookie import write_cookie


class BaseRequest:
    def send_post(self, url, data, cookie=None, get_cookie=None, header=None,files=None):
        '''
        发送post请求
        '''
        if files == None:
            response = requests.post(url=url, data=data, cookies=cookie, headers=header,timeout=5)
        else:
            response = requests.post(url=url, data=data, cookies=cookie, headers=header, timeout=5,files=files)
        if get_cookie != None:
            '''
            {
            "is_cookie":"yes"
            }
            '''
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        httpcode = response.status_code
        return res,httpcode

    def send_get(self, url, data, cookie=None, get_cookie=None, header=None):
        '''
        发送get请求
        '''
        response = requests.get(url=url, params=data, cookies=cookie, headers=header,timeout=5)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        httpcode = response.status_code
        return res,httpcode

    def run_main(self, method, url, data, cookies=None, get_cookie=None, header=None,files=None):
        '''执行方法，传送method,url,参数'''
        # return get_value(url)
        base_url = handle_ini.get_value('pre_host')
        if 'http' not in url:
            url = base_url + url
        if files != None:
            print("请求头部=======>", header)
            print("请求方式========", method)
            print('请求url=======>', url)
            print('请求参数======>', data)
            res,httpcode = self.send_post(url, data, cookies, get_cookie, header,files)
        else:
            if method == 'get':
                print("请求头部=======>",header)
                print("请求方式========",method)
                print('请求url=======>', url)
                print('请求参数======>', data)
                res,httpcode = self.send_get(url, data, cookies, get_cookie, header)

            else:
                print("请求头部=======>", header)
                print("请求方式========", method)
                print('请求url=======>', url)
                print('请求参数======>', data)
                res,httpcode = self.send_post(url, data, cookies, get_cookie, header)


        try:
            res = json.loads(res)
            print("返回结果======>",res)
        except:
            print('这个结果是一个html===========>')
        return res,httpcode


request = BaseRequest()
if __name__ == '__main__':
    request = BaseRequest()

    res = request.run_main(method='post', url='https://t.e.vhall.com/mywebinar/store',
                           data={"subject":"接口测试数据","introduction":"接口测试数据","start_date":"2020-0121","start_time":"10:21","category":"1","img_url":"","topics":"","welcome_content":"","is_auto":"0","rid":"","copy":"","is_new_version":"1","player":"1","buffer":"2","layout":"3","is_chat":"1","is_private":"0","is_open":"1","hide_watch_pv":"0","is_interact":"1"})
    print(res)
