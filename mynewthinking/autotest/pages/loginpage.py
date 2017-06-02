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


    def input_username(self,username):
        ele = self.driver.find_element_by_id(self.files['LoginPage']['Login'][0]['id'])
        self.driver.set_value(ele, (self.files['LoginPage']['Login'][0]['value'])%(username))


    def input_password(self,password):
        ele = self.driver.find_element_by_id(self.files['LoginPage']['Login'][1]['id'])
        self.driver.set_value(ele, (self.files['LoginPage']['Login'][1]['value'])%(password))

        # click login


    def click_login_button(self):
        self.driver.find_element_by_id(self.files['LoginPage']['Login'][2]['id']).click()
        sleep(3)

    def click_logout_button(self):
        self.driver.find_element_by_xpath(self.files['CourseOverViewPage']['Setting'][0]['xpath']).click()
        self.driver.find_element_by_id(self.files['CourseOverViewPage']['settings']['logout']).click()


    def login_action(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    def logout_action(self):
        self.driver.wait_activity(self.files["CourseOverViewPage"]["Activity"], 10)
        self.click_logout_button()

    def course_overview(self):
        self.driver.wait_activity(self.files["CourseOverViewPage"]["Activity"],10)
        #self.driver.find_element_by_id(self.files['CourseOverViewPage']["Download"][0]['id']).click()


