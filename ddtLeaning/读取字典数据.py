import unittest,os
from ddt import ddt,data,unpack,file_data

'''※字典的读取比较特殊，因为在拆分的时候，形参和实参的key值要一致，否则就报错※'''

'''NO.1单组数据'''
@ddt
class Testwork(unittest.TestCase):

    @data({'name':'lili','age':'16'},{'sex':'female','job':'nurser'})
    # @unpack
    def test_01(self,a):
        print(a)

if __name__ == '__main__':
    unittest.main()
结果：
=>{'name': 'lili', 'age': '16'}
  {'sex': 'female', 'job': 'nurser'}
※以上运行的结果数据，就可以用来作为requests的请求参数~！※

'''NO.2多数据拆分，重点来了'''
@ddt
class Testwork(unittest.TestCase):

    @data({'name':'lili','age':'16'},{'name':'female','age':'nurser'})
    @unpack
    def test_01(self,name,age):
        print(name,age)

if __name__ == '__main__':
    unittest.main()
结果：
=>lili 16
  female nurser
※重点来了：首先结果展示的数据是字典里的value，没有打印key的值；其次@data里的数据key值和def方法里的形参
名称一定要一致，否则，打印的时候，就会报莫名的参数错误，这里就不做展示，爱学习的同学可以尝试一下~！※