#coding :utf-8
from APIexcel_config import ExcelConfig
from APIread_excel import ReadExcel
from jsonpath_rw import jsonpath,parse
from APIsend import APISend
import json

class GetData(object):

    def __init__(self):
        self.exceconfig = ExcelConfig()
        self.readexcel = ReadExcel()
        self.apisend = APISend()

    #获取是否运行单元格的内容
    def get_is_run_data(self,row):
        col = self.exceconfig.get_is_run()
        data = self.readexcel.get_excel_data(row,col)
        return data
    #获取url单元格的内容
    def get_url_data(self,row):
        col = self.exceconfig.get_url()
        data = self.readexcel.get_excel_data(row,col)
        return data

    #获取是否有header单元格内容
    def get_is_header(self,row):
        flag = None
        col = self.exceconfig.get_header()
        data = self.readexcel.get_excel_data(row,col)
        if data == "yes":
            flag = self.header_data()
        else:
            flag = None
        return flag

    #header 写死的内容
    def header_data(self):
        data = {
            "Content-Type": "application/json"
        }
        return data

    #获取request_data单元格的数据
    def get_request_data(self,row):
        col = self.exceconfig.get_request_data()
        data = self.readexcel.get_excel_data(row,col)
        return json.loads(data)

    #获取method单元格数据
    def get_method_data(self,row):
        col = self.exceconfig.get_method()
        data = self.readexcel.get_excel_data(row,col)
        return data

    #获取前置条件单元格的内容
    def get_depend_data(self,row):
        col = self.exceconfig.get_depend_data()
        data = self.readexcel.get_excel_data(row,col)
        #通过str.split对字符串进行分割
        data_str = str.split(data,'>')
        # print(data_str)
        return data_str

    #通过分割的前置条件，去第一列查找对应的数据,并获得行号
    def get_case_id_row(self,row):
        col = self.exceconfig.get_case_id()
        col_data = self.readexcel.get_cols(col)
        # print(data)
        row_number = 0
        for cols in col_data:
            if cols == self.get_depend_data(row)[0]:
                row_number = row_number + 1
                return row_number

    #运行依赖的接口，获取响应数据
    def run_depend(self,row):
        row_num = self.get_case_id_row(row)
        method = self.get_method_data(row_num)
        url = self.get_url_data(row_num)
        data = self.get_request_data(row_num)
        header = self.get_is_header(row_num)
        response_data = self.apisend.send_method(method, url, data, header)
        return response_data

    #通过分割的前置条件，去response_data里面解析
    def get_response_depend_data(self,row):
        response = self.run_depend(row)
        jsonpath_expr = parse(self.get_depend_data(row)[1]) #解析
        # print(jsonpath_expr)
        res = jsonpath_expr.find(response)
        return [match.value for match in res][0]




if __name__ == "__main__" :
    getdata = GetData()
    # print( getdata.get_depend_data(2))
    # print(getdata.get_case_id_row(2))
    #
    print(getdata.run_depend(2))
    #
    # print(type(getdata.get_request_data(1)), getdata.get_request_data(1))

    print(getdata.get_response_depend_data(2))

