import json
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

# base_path = os.path.dirname(base_path)
def read_json(file_name=None):
    if file_name==None:
        if '/var/lib/jenkins/workspace/' in base_path:
            file_path = base_path + '/config/mock_data.json'#mock数据用的
        else:
            file_path = os.path.dirname(base_path) + '/config/mock_data.json'
    else:
        if '/var/lib/jenkins/workspace/' in base_path:
            #file_path=base_path+file_name
            file_path = '/var/lib/jenkins/workspace/paas_e/config/header.json'
        else:
            file_path = os.path.dirname(base_path) + file_name
    with open(file_path,encoding='UTF-8') as f:
        data = json.load(f)
    return data


def get_value(key,file_name=None):
    data = read_json(file_name)
    # return data[key]
    return data.get(key)

def write_value(data,filename=None):
    data_value=json.dumps(data)# data是个字典，把字典转换成字符串
    if filename==None:
        if '/var/lib/jenkins/workspace/' in base_path:
            path=base_path+"/config/Cookie.json"
        else:
            path = os.path.dirname(base_path) + "/config/Cookie.json"
    else:
        path=base_path+filename
    with open(path,'w') as f:
        f.write(data_value)

if __name__ == '__main__':
    # print(get_value(key='api3/getcourseintro',file_name='/config/result.json'))
    data={
        'aaa':'bbbbbb'
    }
    write_value(data)