# coding=utf-8
__author__ = 'Anderson'
from time import sleep
from autotest.Base import Base_page
from autotest.public.yamlmanage import YAML

from selenium.webdriver.common.by import By


# driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.Base.capabilities)
class Login(Base_page):
    # usr_input = 'com.ef.core.engage.englishtown:id/txtName'  # password input
    # pwd_input = 'com.ef.core.engage.englishtown:id/txtPwd'
    #
    # # login button
    # login_btn = 'com.ef.core.engage.englishtown:id/btnLogin'
    files= YAML().read_yml("/Users/anderson/testcode/mynewthinking/autotest/pages/pages.yml")
    #usr_input =files[0]['id']


    def input_username(self):
        ele = self.driver.find_element_by_id(self.files['login_page'][0]['id'])
        self.driver.set_value(ele, self.files['login_page'][0]['value'])


    def input_password(self):
        ele = self.driver.find_element_by_id(self.files['login_page'][1]['id'])
        self.driver.set_value(ele, self.files['login_page'][1]['value'])

        # click login


    def click_login_button(self):
        self.driver.find_element_by_id(self.files['login_page'][2]['id']).click()
        sleep(3)


    def login_action(self):
        self.input_username()
        self.input_password()
        self.click_login_button()

    def course_overview(self):
        self.driver.wait_activity(self.files["CourseOverViewPage"]["Activity"],10)
        self.driver.find_element_by_id(self.files['CourseOverViewPage']["Download"][0]['id']).click()

