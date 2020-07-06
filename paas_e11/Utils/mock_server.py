from mitmproxy import http
import sys
import json
import os

base_path = os.getcwd()
sys.path.append(os.path.dirname(base_path))
from Utils.handle_json import get_value


class MockServer:
    def request(self, flow):
        request_data = flow.request
        self.request_url = request_data.url  # 找到请求url
        request_data.host='127.0.0.1'
        request_data.port='5000'


    def response(self, flow):
        if 'laohuangli' in self.request_url or 'juhe' in self.request_url:
            response_data = flow.response
            host = self.request_url.split('.cn')
            # base_url = host[0]
            url = host[1]
            if '?' in host[1]:
                url = url.split("?")[0]
                print('url------>', url)
            data = json.dumps(get_value(url))
            response_data.set_text(data)
addons = [
    MockServer()
]
# mitmdump -p 9999  -s mock_server.py  启动命令