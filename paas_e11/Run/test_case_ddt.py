import os
import sys
import ddt
base_path = os.getcwd()
sys.path.append(base_path)
import unittest
from Utils.handle_excel import excel_data
# data=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8]]
data=excel_data.get_excel_data()
@ddt.ddt
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('case开始执行')

    @ddt.data(*data)
    def test_01(self,data1):
        pass

    def tearDown(self) -> None:
        print('case结束')
if __name__ == '__main__':
    unittest.main()