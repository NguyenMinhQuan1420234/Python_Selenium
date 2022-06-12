import sys
sys.path.append(r"C:\Users\hv\Desktop\FrameworkSample")
import unittest
from pip import main
from Testcase.ExampleSeleniumTestcase import testclasseNumber1
from Testcase.SampleTestcase import SampleTestcase
import HtmlTestRunner


def sampleTestSuite():
    mySuite = unittest.TestSuite()
    mySuite.addTest(testclasseNumber1('test_open_google'))
    mySuite.addTest(testclasseNumber1('test_open_vnexpress'))
    mySuite.addTest(SampleTestcase('test_test1'))
    mySuite.addTest(SampleTestcase('test_test2'))
    return mySuite

def sampleTestSuite2():
    mySuite = unittest.TestSuite()
    mySuite.addTest(testclasseNumber1('test_open_vnexpress'))
    mySuite.addTest(SampleTestcase('test_test1'))
    return mySuite


if __name__ == '__main__':
    mySuite = sampleTestSuite2()
    runner = HtmlTestRunner.HTMLTestRunner(report_title='Sample Report')
    runner.run(mySuite)
    

