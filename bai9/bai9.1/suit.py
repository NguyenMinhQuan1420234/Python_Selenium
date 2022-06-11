import unittest

from testcases import TestCaseSample
import HtmlTestRunner

def sampleTestSuite():
    mySuite = unittest.TestSuite()
    mySuite.addTest(TestCaseSample('test_verify_shoppingButtons'))
    mySuite.addTest(TestCaseSample('test_message_to_customer_service'))
    return mySuite

if __name__ == '__main__':
    mySuite = sampleTestSuite()
    runner = HtmlTestRunner.HTMLTestRunner(report_title='Test Report')
    runner.run(mySuite)
    