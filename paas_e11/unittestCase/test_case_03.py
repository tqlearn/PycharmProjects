import unittest

data = {
    'uesr': '1111'
}
class TestCase03(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Class开始执行')

    def setUp(self):
        print('case开始执行')

    def test_01(self):
        data1 = {
            'uesr': '1112'
        }
        self.assertDictEqual(data1, data)

    def test_02(self):
        data1={
            'uesr':'1111'
        }
        self.assertDictEqual(data1,data)
    def test_03(self):
        a='1112222'
        b='222222'
        self.assertIn(b,a,'不在里面')

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('类执行结束')

if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest(TestCase('test_03'))
    tests=[TestCase03('test_03'),TestCase03('test_01'),TestCase03('test_02')]
    suite.addTests(tests)
    runner=unittest.TextTestRunner()
    runner.run(suite)