# -*- coding: utf-8 -*-
__author__ = 'Anderson'
import unittest
from PO import LevelPage

class Download(unittest.TestCase):

	def setUp(self):
		print "start to test Download"

	def test_download(self):


		LevelPage.download_action()


	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()
	testsuite = unittest.TestSuite()
	testsuite.addTest("test_download")
	testsuite.run()
