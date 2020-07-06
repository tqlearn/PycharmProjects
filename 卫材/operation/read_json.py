#coding : utf-8
import json
class ReadExcel(object):

    def __init__(self,filename):
        self.data = self.read_excel(filename)

    def read_excel(self,filename):
        with open(filename,'rb') as fp:
            data = json.load(fp)
        return data

if __name__ == "__main__":
    filename = '..\config\data.json'
    data = ReadExcel(filename)
    print(data.data)


