#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:chengyanan
@file: mitm.test.py
@time: 2019/10/15  1:26 下午
"""
import sys
import json
import os
from mitmproxy import http,ctx

class GetData:
    def request(self, flow):
        request_data = flow.request
        print(request_data)
        self.request_url = request_data.url  # 找到请求url
        request_pr = request_data.query  # 请求URL查询参数
        self.request_method=request_data.method
        request_form = request_data.urlencoded_form  # 请求POST数据
        # if 't.feeds.antuzhi.com/' in self.request_url:
        #     print( 'Url------------------>',self.request_url)  # 打印请求url
        #     print('request_method-------------->',self.request_method)
        #     # if 're' in request_pr:
        #     print('request_pr--------->%s' % request_pr)  # 打印url查询参数
        #     print('request_form----------->%s' % request_form)  # 打印post数据
        print('Url------------------>', self.request_url)  # 打印请求url
        print('request_method-------------->', self.request_method)
        # if 're' in request_pr:
        print('request_pr--------->%s' % request_pr)  # 打印url查询参数
        print('request_form----------->%s' % request_form)  # 打印post数据


addons = [
    GetData()
]

'''
 mitmdump -p 9999  -s mitm.test.py  执行这个脚本
'''
