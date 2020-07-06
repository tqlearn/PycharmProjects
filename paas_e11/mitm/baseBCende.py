# coding:utf-8

__version = "1.0.0.0"
__date = "Mon Aug 12 14:52:47 CST 2019"
__author = "zhouweiwei"
import os
import sys

base_path = os.getcwd()
sys.path.append(os.path.dirname(base_path))
import requests
import json
import base64
import re
import baseGlobalvar

ENDEAPI = 'http://qa.baice100.com:9009/ende'

_global_dict = {}


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue


try:
    APICONF = baseGlobalvar.get_value('apiconf')
    # APICONF = get_value('apiconf')
except Exception:
    pass
if not APICONF:
    url = ENDEAPI
    postbody = {
        "method": "post",
        "body_type": "GetSupportBodyType"
    }
    headers = None
    response = requests.post(url, postbody, headers)
    if response.status_code != 200:
        print("code is %s" % response.status_code)
    else:
        APICONF = response.content.decode()
        baseGlobalvar.set_value('apiconf', APICONF)
        # set_value('apiconf',APICONF)


def httpReqPost(url, data, headers=None):
    response = requests.post(url, data, headers=headers)
    return response


def reReplase(reg, replaseStr, content, dataDecode=False):
    '''
    @reg: the regex you want to match
    @replase_str: the string you want to replace to
    @content: the string you want to replace
    @dataDecode: if need decode
    '''
    if dataDecode:
        content = content.decode()
    comReg = re.compile(reg)
    m = comReg.search(content)
    if m:
        resultStr = comReg.sub(replaseStr, content)
        return resultStr
    else:
        return content


def ifjson(s):  # judge if josn format
    retstr = s
    if isinstance(retstr, str):
        for i in range(99999):
            nReg = re.compile(r'\n')
            n = nReg.search(retstr)
            if n:
                retstr = reReplase(r'\n\s+', "", retstr)
                retstr = reReplase(r'\n', "", retstr)
            else:
                break
        mReg = re.compile(r'^\{.*}$')
        m = mReg.search(retstr)
        if m:
            return True
    return False


def encode(url, en_data, key=None, transBinData=False, outType=None, body_type=None):
    '''
    @url: api url
    @en_data: need encode data
    @key: project encode key
    @transBinData: if request body is binary, give True
    @outType: not use now
    @body_type: for binary data, if body type is json, give this param
    '''
    endeurl = ENDEAPI
    # request body encode
    en_body = {
        "method": "post",
        "type": "encode",
        "url": url,
        "body_data": en_data
    }
    if transBinData:
        en_body["key"] = key
        en_body["body_type"] = "json"
    elif url == ENDEAPI and not transBinData:  # pushdb
        en_body["key"] = key
    jsonTypeFlag = True
    if ('"%s"' % body_type) in APICONF:
        en_body["body_type"] = body_type
        jsonTypeFlag = False

    headers = None
    response_adreq = httpReqPost(endeurl, en_body, headers)  # if RC4，the return is str, need trans to binary

    data = None
    if response_adreq.status_code != 200:
        print("code is %s" % response_adreq.status_code)
    else:
        resdata_adreq = response_adreq.content.decode()
        if jsonTypeFlag:
            resdata_adreq = json.loads(resdata_adreq)
            data = resdata_adreq["body_data"]
        else:
            data = resdata_adreq
        if transBinData and ("decode_type" in resdata_adreq.keys()):
            if resdata_adreq["decode_type"] == "decode":
                data = data.encode()
                data = base64.b64decode(data)  # str trans to origin binary
        return data
    return None


def decode(url, de_data, key=None, transBinData=False, outType=None, body_type=None, content_type=None):
    '''
    @url: api url
    @de_data: need decode data
    @key: project encode key
    @transBinData: if request body is binary, give True
    @outType: not use now
    @body_type: for binary data, if body type is json, give this param
    @content_type: request content_type
    '''
    endeurl = ENDEAPI
    if not transBinData and isinstance(de_data, bytes):
        de_data = de_data.decode()
    elif transBinData and isinstance(de_data, bytes):  # if binary, trans to str, request decode api
        de_data = base64.b64encode(de_data)
        de_data = de_data.decode()
    # response body decode
    de_body = {
        "method": "post",
        "type": "decode",
        "url": url,
        "body_data": de_data
    }

    if transBinData:
        de_body["key"] = key
        de_body["decode_type"] = "decode"
    elif url == ENDEAPI and not transBinData:  # pushdb
        de_body["key"] = key
        de_body["decode_type"] = "decode"
    jsonTypeFlag = True
    if ('"%s"' % body_type) in APICONF:
        de_body["body_type"] = body_type
        jsonTypeFlag = False
    if content_type:  # for proxy decode (cm)
        de_body["content_type"] = content_type

    headers = None
    response_adresp = httpReqPost(endeurl, de_body, headers)  # if RC4，before decode, need binary trans to str
    data = None
    if response_adresp.status_code != 200:
        print("code is %s" % response_adresp.status_code)
        retresponse = response_adresp.content.decode()
        print(retresponse)
    else:
        retresponse = response_adresp.content.decode()
        if jsonTypeFlag:
            retresponse = json.loads(retresponse)
            data = retresponse["body_data"]
        else:
            data = retresponse
        if transBinData:
            if ifjson(data):
                return json.loads(data)
            return data
        if jsonTypeFlag:
            if ifjson(data):
                return json.loads(data)
            return data
        return data
    return None


def endepost(url, bodydata, key=None, postheaders=None, transBinData=False, body_type=None):
    '''
    @url: api url
    @bodydata: request body data, plaintext
    @key: project encode key
    @postheaders: request headers, dict type
    @transBinData: if request body is binary, give True
    @body_type: for binary data, if body type is json, give this param
    '''
    reqdata = encode(url, bodydata, transBinData=transBinData, body_type=body_type)  # encode request body
    headers = postheaders
    response = httpReqPost(url, reqdata, headers)  # request api

    if response.status_code != 200:
        print("code is %s" % response.status_code)
        print(response.json())
    else:
        if transBinData:
            resdata = response.content
            resdata = base64.b64encode(resdata)
            resdata = resdata.decode()  # if RC4，before decode, need binary trans to str
        else:
            resdata = response.content.decode()
        de_resp = decode(url, resdata, transBinData=transBinData, body_type=body_type)  # decode response body
        return de_resp
    return None


if __name__ == "__main__":
    url = "http://feeds.antuzhi.com/is/rp/v1/enRe?timestamp=1570887761090&pid=gns&pver=5&signature=8bfb99644982a320ef5241df4dafa1ec&nonce=-3081048705006542414&uuid=71ef582cdfcec54fbbdaa34e55a06ba0"
    de_data = b'H4sIAAAAAAAAAAH3AAj/UlF4TXkXXrl2BSTvmuJm/hr5nmS3ron1R/CEvOgeiN5k2R21l8qYGFzu2jB6YiA+HVYMX/KCwEBA+EAhlcuh9mtnUMbF6HfZpNO87iXd84IkzvN+JqsJLKr9gQATyIrEpu4/JAceSqLSR5UouFdp/TGWTEJv/NKQeKHaM29bCPFVca7wuVk7otQRelZib8k/RnqtJH4/QNXMa5A6lL0re2CMRe4sIGDRlao/juDJS5RFWWgN7ps/ImCouj6NHj5s1AD+IuS/pTylsl22BuJ2NWHTe9BpolsKrLah0j4EHTWW1gTSItiFbxRR2yS5ibSQ8ou4KfGIoLs8wET3AAAA'
    ret = decode(url=url, de_data=de_data)
    print(ret)
