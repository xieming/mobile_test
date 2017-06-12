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
        self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["lessonone"]).click()
        time.sleep(2)
        # self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["backbtn"]).click()
        # time.sleep(2)
        # self.login.driver.tap(b, )
        # time.sleep(2)
        modules = self.login.driver.find_elements_by_xpath(iosfile["IOS"]["LoginPage"]["moduleall"])
        # modulesline = self.login.driver.find_elements_by_xpath(iosfile["IOS"]["LoginPage"]["moduleall"])
        # mods = list(filter(lambda e: e % 2 == 0, modules))
        ele = element_exist(self.login.driver)
        for i in range(0, len(modules)):

            modulesline = self.login.driver.find_elements_by_xpath(iosfile["IOS"]["LoginPage"]["moduleach"] % (i))
            for each in modulesline:
                each.click()
                if ele.is_element_exists_by_id(iosfile["IOS"]["LoginPage"]["download"]):
                    self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["download"]).click()
                    time.sleep(20)
                self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["startbtn"]).click()
                time.sleep(2)
                if ele.is_element_exists_by_id(iosfile["IOS"]["LoginPage"]["arrow"]):
                    self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["arrow"]).click()
                    self.login.swipe('down')

                if ele.is_element_exists_by_id(iosfile["IOS"]["LoginPage"]["countiune"]):
                    self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["countiune"]).click()

                if ele.is_element_exists_by_id(iosfile["IOS"]["LoginPage"]["startbtn"]):
                    self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["startbtn"]).click()

                while ele.is_element_exists_by_id(
                    self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["btnQApass"])):
                    self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["btnQApass"]).click()
                    time.sleep(2)

                self.login.driver.find_element_by_id(iosfile["IOS"]["LoginPage"]["btnContinue"]).click()
                time.sleep(2)

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
