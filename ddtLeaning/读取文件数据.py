import unittest,os
from ddt import ddt,data,unpack,file_data

'''数据格式必须为json，且必须为双引号的键值对形式，如果不是json格式，有列表等其它格式嵌套的话，无论是
否有@unpack，形参和参数数量都要和key值相等'''
@ddt
class testwork(unittest.TestCase):
    testdata=[{'a':'lili','b':12},{'a':'sasa','b':66}]
    @data(*testdata)
    # @unpack
    def test_01(self,value):
        print(value)

    @file_data(os.getcwd()+'/jsonll.txt')
    def test_02(self,value2):
        print(value2)

if __name__ == '__main__':
    unittest.main()
结果：
=>{'a': 'lili', 'b': 12}
  {'a': 'sasa', 'b': 66}
  nick
  male
  29