import os
import sys
import json

base_path = os.getcwd()
sys.path.append(base_path)
from Utils.hanlde_heaer import get_header
from Utils.handle_excel import copyexcel, excel_data
from base.base_request import request
from Utils.handle_result import handle_result, handle_result_json, get_result_json
from Utils.handle_cookie import get_cookie_value
from Utils.precondition_data import get_data

test_excel = os.path.dirname(base_path) + '/case/case.xlsx'
report_result = os.path.dirname(base_path) + "/report/api_result.xlsx"


class RunMain:
    def run_case(self):
        copyexcel(test_excel, report_result)
        rows = excel_data.get_rows()
        for i in range(rows):
            cookies = None
            get_cookie = None
            header = None
            data = excel_data.get_row_value(i + 2)
            is_run = data[2]
            if is_run == 'yes':
                is_depend = data[3]
                data1 = json.loads(data[7])  # 把str转换成字典
                if is_depend:  # 获取前置的数据
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    data1[depend_key] = str(depend_data)
                    print('data1-------', data1)
                url = data[5]
                method = data[6]
                cookie_method = data[8]
                is_header = data[9]
                excepect_method = data[10]
                excepect_result = data[11]

                if cookie_method == 'yes':
                    cookies = get_cookie_value('web')
                if cookie_method == 'write':
                    '''
                    先获取cookie
                    '''
                    get_cookie = {'is_cookie': "web"}
                if is_header == 'yes':
                    header = get_header()
                res = request.run_main(method, url, data1, cookies, get_cookie, header)
                try:
                    code = str(res['code'])
                except:
                    print("code报错============》", res)
                try:
                    message = res['errorDesc']
                except:
                    message = 'None'
                if excepect_method == "mec":
                    config_message = handle_result(url, code)
                    print("message------", message, 'config_message-----', config_message)
                    if message == config_message:
                        excel_data.excel_write_data(i + 2, 13, 'pass')
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res, ensure_ascii=False))
                    else:
                        excel_data.excel_write_data(i + 2, 13, 'fail')
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res, ensure_ascii=False))
                if excepect_method == 'errcode':
                    print('-------code---------', excepect_method)
                    if excepect_result == code:
                        excel_data.excel_write_data(i + 2, 13, 'pass')
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res, ensure_ascii=False))
                    else:
                        excel_data.excel_write_data(i + 2, 13, 'fail')
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res, ensure_ascii=False))
                if excepect_method == "json":
                    if code == 1000:
                        status_str = "sucess"
                    else:
                        status_str = 'error'

                    excepect_result = get_result_json(url, status_str)
                    result = handle_result_json(res, excepect_result)
                    if result:
                        print('------', res)
                        excel_data.excel_write_data(i + 2, 13, 'pass')
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res, ensure_ascii=False))
                    else:
                        excel_data.excel_write_data(i + 2, 13, 'fail')
                        excel_data.excel_write_data(i + 2, 14, json.dumps(res, ensure_ascii=False))


if __name__ == '__main__':
    runmain = RunMain()
    runmain.run_case()
