# -*- coding: utf-8 -*-
__author__ = 'Anderson'
from ptest.assertion import assert_that
from ptest.decorator import TestClass, Test, BeforeMethod

from autotest.pages.loginpage import Login


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        # self.username = 'newqa@qp1.org'
        # self.password = '11111111'
        print("start to test")

    @Test()
    def check_login_success(self):
        login = Login()
        login.login_action()
        login.course_overview()
