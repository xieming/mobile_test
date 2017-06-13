# -*- coding: utf-8 -*-
__author__ = 'Anderson'
import time

from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod
from ptest.plogger import preporter

from autotest.pages.loginpage import Login
from autotest.public.yamlmanage import YAML
from autotest.public.imagehelper import Appium_Extend
from autotest.public.elementhelper import element_exist


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        self.login = Login()
        self.username = 'dd2@qp1.org'
        self.password = '1'
        print("start to test")

    @Test()
    def check_login_success1(self):
        yml = YAML()
        iosfile = yml.read_yml("/Users/anderson/testcode/mynewthinking/autotest/pages/pages.yml")
        print(iosfile["Android"]["LoginPage"]["username"])
        ele = self.login.find_element(iosfile["Android"]["LoginPage"]["username"])
        print(ele)
        self.login.driver.set_value(ele, self.username)
        time.sleep(2)
        ele = self.login.find_element(iosfile["Android"]["LoginPage"]["password"])
        print(ele)
        self.login.driver.set_value(ele, self.password)
        time.sleep(2)
        self.login.find_element(iosfile["Android"]["LoginPage"]["loginbtn"]).click()
        time.sleep(20)

    @Test()
    def check_login_success(self):
        self.login.login_action(self.username, self.password)
        self.login.course_overview()
        time.sleep(8)
        self.login.logout_action()

    @Test()
    def check_login_success_ios(self):
        # self.login.login_action(self.username, self.password)
        # self.login.course_overview()
        # time.sleep(8)
        # self.login.logout_action()
        yml = YAML()
        iosfile = yml.read_yml("/Users/anderson/testcode/mynewthinking/autotest/pages/pages.yml")
        ele = self.login.driver.find_element_by_xpath(iosfile["IOS"]["LoginPage"]["username"])
        print(ele)
        self.login.driver.set_value(ele, self.username)
        time.sleep(2)
        ele = self.login.driver.find_element_by_xpath(iosfile["IOS"]["LoginPage"]["password"])
        print(ele)
        self.login.driver.set_value(ele, self.password)
        time.sleep(2)
        self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["loginbtn"]).click()
        time.sleep(20)
        # self.login.swipe('down')
        # self.login.swipe('up')
        # # self.login.driver.find_element_by_ios_predicate('type == "XCUIElementTypeOther" AND label == "Profile"').click()
        # print(iosfile["IOS"]["LoginPage"]["settings"])
        # location = self.login.driver.find_element_by_xpath(iosfile["IOS"]["LoginPage"]["settings"])
        # print(location)
        # print(location.size)
        # pic = Appium_Extend(self.login.driver)
        # a, b, c = pic.get_location_by_element(location, 3)
        # print("course")
        # print(a)
        # print("classroom")
        # print(b)
        # print("setting")
        # print(c)
        # self.login.driver.tap(c, )
        # time.sleep(2)
        # self.login.driver.tap(a, )
        # time.sleep(2)

    @Test()
    def pass_one_lesson(self):
        self.login.login_action(self.username, self.password)
        self.login.pass_one_lesson()
        # self.login.logout_action()

    @Test()
    def pass_one_unit(self):
        self.login.login_action(self.username, self.password)
        self.login.pass_one_unit()
        # self.login.logout_action()

    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("cleaning up")
        self.login.driver.quit()
        # self.login.driver.close_app()
