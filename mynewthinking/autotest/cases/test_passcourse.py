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
from globals import PLATFORM,get_current_package
from setupenv import setup_env,clear_catch

@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        #setup_env()
        self.login = Login()
        self.username = 'newqa@qp1.org'
        self.password = '11111111'
        print("start to test")
        self.course = Course(self.login.driver)


    @Test()
    def pass_one_lesson(self):

        self.login.login_action(self.username,self.password)
        self.course.pass_one_lesson_action("lessontwo")
        self.course.logout_action()

    @Test()
    def pass_one_unit(self):

        self.login.login_action(self.username,self.password)
        self.course.pass_one_unit_action()
        self.course.logout_action()


    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("cleaning up")
        clear_catch(get_current_package())
        self.login.driver.quit()
        # self.login.driver.close_app()
