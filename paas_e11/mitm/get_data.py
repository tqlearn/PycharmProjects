from mitmproxy import http
import os
import sys

base_path = os.getcwd()
sys.path.append(base_path)
from Utils.handle_json import get_value


class GetData:
    def request(self, flow):
        request_data = flow.request
        print(request_data)
        self.request_url = request_data.url  # 找到请求url
        request_pr = request_data.query  # 请求URL查询参数
        request_form = request_data.urlencoded_form  # 请求POST数据
        print('url---------->%s' % self.request_url)  # 打印请求url
        print('request_pr--------->%s' % request_pr)  # 打印url查询参数
        print('request_form----------->%s' % request_form)  # 打印post数据

    def response(self, flow):
        # if 'laohuangli' in self.request_url or 'juhe' in self.request_url:
        response_data = flow.response
        host = self.request_url.split('.cn')[0]
        base_url = host[0]
        # http://v.juhe.cn/laohuangli/d
        # http://v.juhe.cn/laohuangli/d?key=123&date=2019-09-09
        if '?' in host[1]:
            url = host[1].split('?')[0]
        data = get_value(url)
        print('get_data========-------->', data)
        response_data.set_text(data)
        '''
         response_header = response_data.headers
         conten_type = response_header['Content-Type']
         print('=========>',conten_type)
         if conten_type=='imag/jpeg':
             print('这个返回的是图片格式')
         elif 'json' in conten_type:
             print('code===========>',response_data.status_code)
             print('response========>',response_data.text)
         else:
             print('格式不是我们预期的')
         '''


addons = [
    GetData()
]
