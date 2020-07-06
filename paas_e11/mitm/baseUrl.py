#coding:utf-8
from urllib import parse
import json
import re
import os
import sys
base_path = os.getcwd()
sys.path.append(os.path.dirname(base_path))
def reReplase(reg,replaseStr,content,dataDecode=False):
    if dataDecode:
        content = content.decode()
    comReg = re.compile(reg)
    m = comReg.search(content)
    if m:
        resultStr = comReg.sub(replaseStr,content)
        return resultStr
    else:
        return content

def transUrlToList(url): # url 中的参数 转为列表
    try:
        result = parse.urlparse(url)
        query_dict = parse.parse_qs(result.query)
        listKeys = list(query_dict.keys())
        listValues = list(query_dict.values())
        for l in range(len(listValues)):
            listValues[l].insert(0, listKeys[l])
        if listValues:
            return listValues
        return None
    except Exception:
        return None

def transUrlToDict(url): # url 中的参数 转为字典
    try:
        result = parse.urlparse(url)
        query_dict = parse.parse_qs(result.query)
        if query_dict:
            return query_dict
        return None
    except Exception:
        return None
    
def getUrlParamValue(url, key): #获取需要的信息
    try:
        result = parse.urlparse(url)
        query_dict = parse.parse_qs(result.query) # url里的查询参数  
        getvalue = query_dict.get(key)
        if getvalue:
            return getvalue[0]
        return None
    except Exception:
        return None

def getUrlHostAndPort(url): # 获取url的host
    try:
        result = parse.urlparse(url)
        hostaddr = result.netloc
        if hostaddr:
            return hostaddr
        return None
    except Exception:
        return None
    
def urlEncode(encodStr): # url 编码
    try:
        ret = parse.quote(encodStr)
        if ret:
            return ret
        return None
    except Exception:
        return None

def urlDecode(decodeStr): # url 解码
    try:
        ret = parse.unquote(decodeStr)
        if ret:
            return ret
        return None
    except Exception:
        return None

def unquoteUrl(url, dataDecode=False, typeJson=False): # url 解码 输出格式
    try:
        if dataDecode:
            url = url.decode()
        urldata = urlDecode(url)
        if urldata:
            if typeJson:
                return json.loads(urldata)
            return urldata
        return None
    except Exception:
        return None

def ifUrlMatch(reg, url):
    if_flag = False
    comReg = re.compile(reg)
    m = comReg.search(url)
    if m:
        if_flag = True
    return if_flag

if __name__ == "__main__":
    print("done!")
