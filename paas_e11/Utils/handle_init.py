import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
import configparser

class HandInit:
    def load_ini(self):
        file_path = os.path.dirname(base_path) + '/config/server.ini'
        cf=configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8-sig')
        return cf

    def get_value(self,key,section=None):
        '''获取ini里的value'''
        if section==None:
            section='server'
        cf=self.load_ini()
        try:
            data = cf.get(section, key)
        except Exception:
            print('---------没有获取到值-----------')
            data=None
        return data
handle_ini=HandInit()
if __name__ == '__main__':
    hd=HandInit()
    print(hd.load_ini())
    # print(hd.get_value('host'))
