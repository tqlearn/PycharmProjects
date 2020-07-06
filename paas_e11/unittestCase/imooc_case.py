import sys
import os
import MOCK
import unittest
import json
import HTMLTestRunner

base_path = os.getcwd()
sys.path.append(base_path)
from base.base_request import request

base_path = os.path.dirname(base_path)
json_path = base_path + '/config/mock_data.json'
print(json_path)


def read_json():
    with open(json_path) as f:
        data = json.load(f)
    return data


def get_value(key):
    data = read_json()
    return data[key]


header = {
    'cp-os': 'android',
    'cp-ver': '1.1.45',
    'cp-uuid': 'test12311133345',
    'cp-abid': '6-100',
    'cp-channel': 'huawei_market',
    'cp-time': '1556425865',
    'cp-token': '-GzKz1I3fE-s4QGJzbXPmLlSAQCj8uUvra9KWQYh23I_',
    'cp-oem': 'Xiaomi',
    'cp-sver': '9',
    'cp-sign': 'd58ee706473b44ec3b1089fd75222b73',
    'cp-appid': '800',
    'Host': 'api.kuai8.mobi',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.3.1',
    'Connection': 'keep-alive'
}
host = 'http://api.kuai8.mobi'


class ImoocCase(unittest.TestCase):
    def test_banner(self):
        url = host + '/1/feed/list.json'
        params = {
            "count": 15,
            "page": 1
        }
        mock_method = MOCK.Mock(return_value=get_value("/config/mock_data.json"))
        request.run_main = mock_method
        res = request.run_main('get', url=url, params=params, headers=header)
        self.assertEqual(res['status'], 500)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ImoocCase('test_banner'))
    file_path = base_path + '/report/report.html'
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='nannan测试')
        runner.run(suite)
    f.close()
