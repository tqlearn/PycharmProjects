import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from Utils.handle_json import get_value
from deepdiff import DeepDiff

# print(get_value("api3/getbanneradvertver2","code_message.json"))
'''
    "api3/getcourseintro":[
        {"1006":"token error"},
        {"10001":"用户名错误"},
        {"10002":"密码错误"}
    ]
'''


def handle_result(url, code):
    data = get_value(url, "/config/code_message.json")
    if data != None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None


def handle_result_json(dict1, dict2):
    '''校验格式'''
    # dict1 = {"aaa": "AAA", "bbb": "BBBB", "CC": [{"11": "22"}, {"11": "44"}]}
    # dict2 = {"aaa": "123", "bbb": "456", "CC": [{"11": "111"}, {"11": "44"}]}
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()  # ignore_order=True列出不同的地方
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False

def get_result_json(url, status):
    data = get_value(url, "/config/result.json")
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None


if __name__ == '__main__':
    # print(handle_result("feed/list.json", "1006"))
    # dict1 = {"aaa": "AAA", "bbb": "BBBB", "CC": [{"11": "22"}, {"11": "44"}]}
    # dict2 = {"aaa": "123", "bbb": "456", "CC": [{"11": "111"}, {"11": "44"}]}
    # print(handle_result_json(dict1, dict2))
    # print(get_result_json("api3/getcourseintro","sucess")
    print(get_result_json('http://v.juhe.cn/laohuangli/d','sucess'))
