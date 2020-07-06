import unittest
import sys
import os
sys.path.append('/Users/chengyanan/Desktop/Venv_data/interfaceTest')
from unittestCase.test_case01 import TestCase01
from unittestCase.test_case_02 import TestCase02
from unittestCase.test_case_03 import TestCase03

# case01=unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case02=unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case03=unittest.TestLoader().loadTestsFromTestCase(TestCase03)
# tests=[case01,case02,case03]
# suite=unittest.TestSuite(tests)
# unittest.TextTestRunner().run(suite)
case_path=os.getcwd()+'/unittestCase/'
discover=unittest.defaultTestLoader.discover(case_path,'test_case*.py')
unittest.TextTestRunner().run(discover)