from mitmproxy import http
import sys
import json
import os

base_path = os.getcwd()
sys.path.append(os.path.dirname(base_path))
from Utils.handle_json import get_value


class GetData:
    def request(self, flow):
        request_data = flow.request
        print(request_data)
        self.request_url = request_data.url  # 找到请求url
        request_pr = request_data.query  # 请求URL查询参数
        request_form = request_data.urlencoded_form  # 请求POST数据
        if 'enRe' in self.request_url:
            print('url---------->%s' % self.request_url.split("?")[0])  # 打印请求url
            print('request_pr--------->%s' % str(request_pr))  # 打印url查询参数
            print('type------>',type(request_pr))
            print('request_form----------->%s' % request_form)  # 打印post数据

    # def response(self, flow):
    #     if 'laohuangli' in self.request_url or 'juhe' in self.request_url:
    #         response_data = flow.response
    #         host = self.request_url.split('.cn')
    #         base_url = host[0]
    #         url = host[1]
    #         print('url==========', url)
    #         if '?' in host[1]:
    #             url = url.split("?")[0]
    #             print('url------>', url)
    #         data = json.dumps(get_value(url))
    #         # print('data--------->', data)
    #         response_data.set_text(data)
    #         response_header = response_data.headers
    #         conten_type = response_header['Content-Type']
    #         print('=========>', conten_type)
    #         print('response========>', response_data.text)

            # print('=========>',conten_type)
            # if conten_type=='imag/jpeg':
            #     print('这个返回的是图片格式')
            # elif 'json' in conten_type:
            #     print('code===========>',response_data.status_code)
            #     print('response========>',response_data.text)
            # else:
            #     print('格式不是我们预期的')


addons = [
    GetData()
]
