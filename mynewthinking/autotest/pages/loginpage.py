# coding=utf-8
__author__ = 'Anderson'
from autotest.Base import Base_page
from autotest.public.yamlmanage import YAML
import time
from globals import WAIT_TIME,WAIT_MINI_TIME


class Login(Base_page):
    page = YAML().current_page('LoginPage')
    username = page['username']
    password = page['password']
    loginbtn = page['loginbtn']
    coursepage = YAML().current_page('CourseOverViewPage')
    downloadbtn = coursepage['Download']



    def login_action(self, username, password):
        self.wait_for_visibility_of_element_located(self.loginbtn)
        self.type(self.username, username)
        self.type(self.password, password)
        self.clickat(self.loginbtn)
        #time.sleep(WAIT_MAX_TIME)
        self.wait_for_presence_of_element_located(self.downloadbtn)
        time.sleep(WAIT_MINI_TIME)



    def open_app_android(self,username, password):
        login_page_activity = self.page["Activity"]
        if self.driver.current_activity == login_page_activity:
            self.login_action(username, password)


