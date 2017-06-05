# -*- coding: utf-8 -*-
__author__ = 'Anderson'
import time

from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod
from ptest.plogger import preporter

from autotest.pages.loginpage import Login


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        self.login = Login()
        self.username = 'dd2@qp1.org'
        self.password = '1'
        print("start to test")

    @Test()
    def check_login_success(self):
        self.login.login_action(self.username, self.password)
        self.login.course_overview()
        time.sleep(8)
        self.login.logout_action()

    @Test()
    def pass_one_lesson(self):
        self.login.login_action(self.username, self.password)
        self.login.pass_one_lesson()
        #self.login.logout_action()

    @Test()
    def pass_one_unit(self):
        self.login.login_action(self.username, self.password)
        self.login.pass_one_unit()
        #self.login.logout_action()

    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("cleaning up")
        self.login.driver.quit()
        # self.login.driver.close_app()
