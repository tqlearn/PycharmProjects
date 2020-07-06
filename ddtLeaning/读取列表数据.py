import unittest,os
from ddt import ddt,data,unpack,file_data

'''NO.1单组元素和多组元素未分解都一样,下面看嵌套，考眼力了~'''
@ddt
class Testwork(unittest.TestCase):

    @data([{'name':'lili','age':12},{'sex':'male','job':'teacher'}])
    # @unpack
    def test_01(self,a):
        print(a)

if __name__ == '__main__':
    unittest.main()
结果：
=>[{'name': 'lili', 'age': 12}, {'sex': 'male', 'job': 'teacher'}]
※上面结果可以看出：无法运用到requests数据请求中，所以不是很实用※

'''NO.2多组元素分解'''
@ddt
class Testwork(unittest.TestCase):

    @data([{'name':'lili','age':12},{'sex':'male','job':'teacher'}])
    @unpack
    def test_01(self,a,b):
        print(a,b)

if __name__ == '__main__':
    unittest.main()
结果：
=>{'name': 'lili', 'age': 12} {'sex': 'male', 'job': 'teacher'}
※拆分后的运行结果，不带有[ ]，拆分是将列表中的2个字典拆分，所以有2个数据※