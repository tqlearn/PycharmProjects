#coding :utf-8

class ExcelConfig(object):

    def __init__(self):
        #case编号
        self.case_id = 0
        #作用
        self.message = 1
        #是否执行
        self.is_run = 2
        #前置条件
        self.depend_data = 3
        #依赖Key
        self.depend_key = 4
        #url
        self.url = 5
        #method
        self.method = 6
        #data
        self.request_data = 7
        #Cookie操作
        self.cookie = 8
        #Header操作
        self.header = 9
        #预期结果
        self.expect = 10
        #result
        self.result = 11
        #返回数据
        self.response_data = 12

    def get_case_id(self):
        return self.case_id

    def get_message(self):
        return self.message

    def get_is_run(self):
        return self.is_run

    def get_depend_data(self):
        return self.depend_data

    def get_depend_key(self):
        return self.depend_key

    def get_url(self):
        return self.url

    def get_method(self):
        return self.method

    def get_request_data(self):
        return self.request_data

    def get_cookie(self):
        return self.cookie

    def get_header(self):
        return self.header

    def get_expect(self):
        return self.expect

    def get_result(self):
        return self.result

    def get_response_data(self):
        return self.request_data
