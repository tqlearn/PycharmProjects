# coding = utf - 8
import requests
import unittest
import mock

url = "http://www.imooc.com/login"
data = {
    "username": "111111",
    "password": "11222"
}


def post_request(url, data):
    res = requests.post(url, data).json()
    return res


def get_request(url, data):
    res = requests.get(url=url, params=data).json()
    return res


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case执行结束")

    def test_01(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username": "33333",
            "password": "44444"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("11222", res())

    def test_02(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username": "33333",
            "password": "44444"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("11222", res())

    def test_03(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username": "33333",
            "password": "44444"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("11222", res())

    def test_04(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username": "33333",
            "password": "44444"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("11222", res())

    def test_05(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username": "33333",
            "password": "44444"
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request
        self.assertEqual("11222", res())

#java -jar moco-runner-0.12.0-standalone.jar start -p 9910 -c config.json执行mock server
if __name__ == '__main__':
    unittest.main()
