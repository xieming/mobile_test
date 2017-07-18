# coding=utf-8
__author__ = 'Anderson'
from autotest.Base import Base_page
from autotest.public.yamlmanage import YAML
import time


class Login(Base_page):
    page = YAML().current_page('LoginPage')
    username = page['username']
    password = page['password']
    loginbtn = page['loginbtn']


    def login_action(self, username, password):
        time.sleep(3)
        self.type(self.username, username)
        self.type(self.password, password)
        self.clickat(self.loginbtn)

    def open_app_android(self,username, password):
        login_page_activity = self.page["Activity"]
        if self.driver.current_activity == login_page_activity:
            self.login_action(username, password)


