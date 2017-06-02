# -*- coding: utf-8 -*-
__author__ = 'Anderson'
from ptest.assertion import assert_that
from ptest.decorator import TestClass, Test, BeforeMethod

from autotest.pages.loginpage import Login
from autotest.public.imagehelper import IMAGE
import time


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        self.username = 'newqa@qp1.org'
        self.password = '11111111'
        print("start to test")

    @Test()
    def check_login_success(self):
        login = Login()
        login.login_action(self.username,self.password)
        login.course_overview()
        time.sleep(8)
        login.logout_action()
        #IMAGE().get_picture("//android.widget.ImageView[@index='0']")
