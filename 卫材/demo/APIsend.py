#coding : utf-8
import requests
class APISend(object):

    def __init__(self):
        pass

    def send_get(self,url,data,header=None):
        res = requests.get("https://test-api.vhallyun.com" + url,data,header)
        return res.json()

    def send_post(self,url,data,header=None):
        res = requests.post("https://test-api.vhallyun.com" + url,data,header)
        return res.json()

    def send_method(self,method,url,data,header=None):
        if method == 'post':
            res = self.send_post(url,data,header)
        else:
            res = self.send_get(url,data,header)
        return res

if __name__ == "__main__" :
    send = APISend()
    url = '/api/v1/base/create-v2-access-token'
    data = {"third_party_user_id":"zx","app_id":"d317f559","signed_at":"12345","sign":"vhall","data_collect_manage":"all","data_collect_view":"all","data_collect_submit":"all"}
    res = send.send_method('post',url,data)
    print(res)