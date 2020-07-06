import sys
import os
import json

base_path = os.getcwd()
sys.path.append(base_path)
from Utils.handle_excel import excel_data
from jsonpath_rw import parse

'''
前置条件的操作
'''


def split_data(data):
    # test_api001>data:banner:id
    #data=test_api001>data
    case_id = data.split(">")[0]#case_id=test_api001
    rule_data = data.split('>')[1]#rule_data=data
    return case_id, rule_data


def depaned_data(data):
    '''
    获取前置条件的依赖数据结果集
    :return:
    '''
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id)#获取case_id所在的行号
    data = excel_data.get_cell_value(row_number, 14)#获取case_id的返回数据
    return data


def get_depend_data(res_data, key):
    '''
    获取依赖字段
    '''
    #key=========== c.[1].d
    res_data = json.loads(res_data)  # 字符串转换成字典
    #res_data======= {'a': 'a1', 'b': 'b', 'c': [{'d': 'd1'}, {'d': 'd2'}]}
    json_exe = parse(key)
    #json_exe=====> c.[1].d
    madle = json_exe.find(res_data)#在res_data中找c.[1].d对应的值
    return [math.value for math in madle][0]


def get_data(data):
    '''获取依赖数据'''
    #data=test_api_016>data
    res_data = depaned_data(data)
    #res_data={"code": "200", "msg": "成功", "data": 188653368}
    rule_data = split_data(data)[1]
    #rule_data=data
    return get_depend_data(res_data, rule_data)
def get_id(detail,id,answer):
    detail = json.loads(detail.replace("'", '"').replace('None', '""'))
    ids = []
    for i in range(len(detail)):
        idf = detail[i][id]
        ids.append(idf)
    answer = answer.replace("'",'"').replace('None', '""')
    answer = dict(json.loads(answer))
    ansy = []
    for k, y in answer.items():
        ansy.append(y)
    return json.dumps(dict(zip(ids, ansy)))

if __name__ == '__main__':
    data = {
        "a": "a1",
        "b": "b",
        "c": [
            {"d": "d1"},
            {
                "d": "d2"},
        ]
    }
    data = json.dumps(data)
    key = 'c.[1].d'
    get_data("test_api_016>data")
