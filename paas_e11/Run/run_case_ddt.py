# encoding: utf-8
import os
import sys
import ddt

base_path = os.getcwd()
sys.path.append(base_path)
sys.path.append(os.path.dirname(base_path))
from base import HTMLTestRunner
import unittest
from Utils.handle_excel import excel_data, copyexcel
test_excel = os.path.dirname(base_path) + '/case/case.xlsx'
report_result = os.path.dirname(base_path) + "/report/api_result.xlsx"
copyexcel(test_excel, report_result)
data = excel_data.get_excel_data()
import json
from Utils.hanlde_heaer import get_header
from Utils.handle_excel import excel_data
from base.base_request import request
from Utils.handle_result import handle_result, handle_result_json, get_result_json
from Utils.handle_cookie import get_cookie_value
from Utils.precondition_data import get_data,get_id
from Utils.send_mail import sendMail
import datetime
import time

@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):
    @ddt.data(*data)
    def test_main_case(self, data):
        cookies = None
        get_cookie = None
        header = None
        is_run = data[2]
        case_id = data[0]
        Interface_name=data[1]
        isjson = data[14]
        i = excel_data.get_rows_number(case_id)
        if is_run == 'yes':
            data1 = json.loads(data[7])
            if isjson != None: #判断是否有字典要求必须是json格式
                isjson = isjson.split('/')
                for n in isjson:
                    data1[n] = json.dumps(data1[n])
            print("接口名称====", Interface_name)
            is_depend = data[3]
            try:
                if is_depend:  # 获取前置的数据
                    is_depend = is_depend.split('/')
                    data4 = data[4].split('/')
                    d = dict(map(lambda x,y:[x,y],data4,is_depend))
                    for k,y in d.items():
                        depend_key = k
                        depend_data = get_data(y)
                        if data[15] == "yes":
                            data1[depend_key] = str(depend_data).replace('[','').replace(']','')
                        else:
                            if "[" in str(depend_data) or "{" in str(depend_data):
                                data1[depend_key] = get_id(str(depend_data), data[16], str(data1[data[17]]))
                            else:
                                data1[depend_key] = depend_data
                        #data1[depend_key] = depend_data

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
                if data[19] == "yes":
                    start_time = datetime.datetime.now()
                    s = datetime.timedelta(seconds=5)
                    start_times = (start_time+s).strftime('%Y-%m-%d %H:%M:%S')
                    es = datetime.timedelta(seconds=43)
                    end_time = (start_time+es).strftime('%Y-%m-%d %H:%M:%S')
                    data1["start_time"] = start_times
                    data1["end_time"] = end_time
                if data[20] != None:
                    num = data[20]
                    time.sleep(num)
                if data[18] != None:
                    file = json.loads(data[18])
                    for key in file:
                        if "/var/lib/paas_e/fileaddres" in file[key]:
                            files = {key:(open(file[key],"rb"))}
                        else:
                            files = {key: (open(file[key], "rb"))}
                    res,httpcode= request.run_main(method, url, data1, cookies, get_cookie, header,files)
                    code = str(res['code'])
                else:
                    res,httpcode = request.run_main(method, url, data1, cookies, get_cookie, header)
                    code = str(res['code'])

                try:
                    message = res['reason']
                except:
                    message = None

                if excepect_method == "mec":
                    config_message = handle_result(url, code)
                    '''   
                    if message == config_message:
                        excel_data.excel_write_data(i, 12, 'pass')
                        excel_data.excel_write_data(i, 13, json.dumps(res, ensure_ascii=False))
                    else:
                        excel_data.excel_write_data(i, 12, 'fail')
                        excel_data.excel_write_data(i, 13, json.dumps(res, ensure_ascii=False))
                '''
                    try:
                        self.assertEqual(message, config_message)
                        excel_data.excel_write_data(i, 13, 'pass')
                        excel_data.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, 'fail')
                        excel_data.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))
                        raise e
                if excepect_method == 'errcode':
                    '''
                    print('-------code---------', excepect_method)
                    if excepect_result == code:
                        excel_data.excel_write_data(i, 12, 'pass')
                        excel_data.excel_write_data(i, 13, json.dumps(res, ensure_ascii=False))
                    else:
                        excel_data.excel_write_data(i, 12, 'fail')
                        excel_data.excel_write_data(i, 13, json.dumps(res, ensure_ascii=False))
                    '''
                    try:
                        self.assertEqual(str(excepect_result), code)
                        print('预计结果: ', excepect_result)
                        print("实际结果: ",code)
                        print("Http状态码：",httpcode)
                        excel_data.excel_write_data(i, 13, 'pass')
                        excel_data.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, 'fail')
                        excel_data.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))
                        raise e

                if excepect_method == "json":
                    if code == '0':
                        status_str = "sucess"
                    else:
                        status_str = 'error'

                    excepect_result = get_result_json(url, status_str)
                    result = handle_result_json(res, excepect_result)
                    print('预期结果---->', excepect_result)
                    print('实际结果---->', res)
                    '''
                    if result:
                        print('------', res)
                        excel_data.excel_write_data(i, 12, 'pass')
                        excel_data.excel_write_data(i, 13, json.dumps(res, ensure_ascii=False))
                    else:
                        excel_data.excel_write_data(i, 12, 'fail')
                        excel_data.excel_write_data(i, 13, json.dumps(res, ensure_ascii=False))
                    '''
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i, 13, 'pass')
                        excel_data.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        excel_data.excel_write_data(i, 13, 'fail')
                        excel_data.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))
                        raise e
            except Exception as e:
                excel_data.excel_write_data(i, 13, 'fail')
                excel_data.excel_write_data(i, 14, json.dumps(res, ensure_ascii=False))

                raise e


if __name__ == '__main__':
    sendmail = sendMail()
    case_path = base_path
    data = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    data = 'report'+str(data)+'.html'
    if "/var/lib/jenkins/workspace/" in base_path:
        #report_path = base_path + '/report/report.html'
        report_path = '/var/lib/jenkins/workspace/paas_e/report/'+data
    else:
        report_path = os.path.dirname(base_path) + '/report/'+data
    discover = unittest.defaultTestLoader.discover(case_path, pattern='run_case_*.py')
    #unittest.TextTestRunner.run(discover)
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', description='PAAS测试报告', tester="yanan.cheng")
        runner.run(discover)
    if excel_data.get_success_result():
        print("全部通过")
        print("测试报告地址：http://172.16.11.105/"+data)
    else:
        print("有用例执行失败,发邮件中")
        print("测试报告地址：http://172.16.11.105/" + data)
        #sendmail.sen_mail()
