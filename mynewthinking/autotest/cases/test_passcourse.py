# -*- coding: utf-8 -*-
__author__ = 'Anderson'
import time

from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod
from ptest.plogger import preporter

from autotest.pages.loginpage import Login
from autotest.pages.courseoverviewpage import Course
from autotest.public.yamlmanage import YAML
from autotest.public.imagehelper import Appium_Extend
from autotest.public.elementhelper import element_exist


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        self.login = Login()
        self.username = 'newqa@qp1.org'
        self.password = '11111111'
        print("start to test")
        self.course = Course(self.login.driver)


    @Test()
    def pass_one_lesson(self):
        self.login.login_action(self.username, self.password)

        self.course.logout_action()

    @Test()
    def pass_one_unit(self):
        if self.login.driver.current_activity == self.login.login_page_activity:
            self.login.login_action(self.username, self.password)

        self.course.pass_one_unit_action()
        self.course.logout_action()


    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("cleaning up")
        self.login.driver.quit()
        # self.login.driver.close_app()
