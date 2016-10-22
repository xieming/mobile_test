#coding=utf-8
__author__ = 'Anderson'
import unittest
from Public import HTMLTestRunner
import time
import os


case_path = os.getcwd() + "/TestCase/"
result = os.getcwd() + "/Result/"

def Creatsuite():

    testunit = unittest.TestSuite()


    discover = unittest.defaultTestLoader.discover(case_path, pattern='Test_*.py', top_level_dir=None)


    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
    return testunit

test_case = Creatsuite()

now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))


tdresult = result + day
if os.path.exists(tdresult):
    filename = tdresult + "/" + now + "_result.html"
    fp = file(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Engage Test Report', description=u'Detail：')


    runner.run(test_case)
    fp.close()
else:
    os.mkdir(tdresult)
    filename = tdresult + "/" + now + "_result.html"
    fp = file(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Engage Test Report', description=u'Detail：')


    runner.run(test_case)
    fp.close()
