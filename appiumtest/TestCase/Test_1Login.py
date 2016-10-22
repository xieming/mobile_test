# -*- coding: utf-8 -*-
__author__ = 'Anderson'
import unittest
from PO import LoginPage

class Login(unittest.TestCase):

	def setUp(self):
		print "start to test login"

	def test_Login(self):
		username='dla_none_cn@qp1.org'
		password='11111111'

		LoginPage.login_action(username, password)


	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()
	#testsuite = unittest.TestSuite()
	#testsuite.addTest("test_Search")
	#testsuite.run()
