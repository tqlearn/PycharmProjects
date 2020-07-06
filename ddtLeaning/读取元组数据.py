'''
一般进行接口测试时，每个接口的传参都不止一种情况，一般会考虑正向、逆向等多种组合。所以在测试一个接口时通常会编写多条case，而这些case除了传参不同外，其实并没什么区别。
这个时候就可以利用ddt来管理测试数据，提高代码复用率。
※但要注意：正向和逆向的要分开写※
安装：pip install ddt
四种模式：第一步引入的装饰器@ddt；导入数据的@data；拆分数据的@unpack；导入外部数据的@file_data
'''




# 一定要和单元测试框架一起用
import unittest, os
from ddt import ddt, data, unpack, file_data

'''NO.1单组元素'''


@ddt
class Testwork(unittest.TestCase):

    @data(1, 2, 3)
    def test_01(self, value):  # value用来接收data的数据
        print(value)


if __name__ == '__main__':
    unittest.main()
结果：
= > 1
2
3

'''NO.2多组未分解元素'''


@ddt
class Testwork(unittest.TestCase):

    @data((1, 2, 3), (4, 5, 6))
    def test_01(self, value):
        print(value)


if __name__ == '__main__':
    unittest.main()
结果：
= > (1, 2, 3)
(4, 5, 6)

'''NO.3多组分解元素'''


@ddt
class Testwork(unittest.TestCase):

    @data((1, 2, 3), (4, 5, 6))
    @unpack  # 拆分数据
    def test_01(self, value1, value2, value3):  # 每组数据有3个值，所以设置3个形参
        print(value)


if __name__ == '__main__':
    unittest.main()
结果：
= > 1
2
3
4
5
6