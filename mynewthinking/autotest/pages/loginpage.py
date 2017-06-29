# coding=utf-8
__author__ = 'Anderson'
from autotest.Base import Base_page
from autotest.public.yamlmanage import YAML


class Login(Base_page):
    page = YAML().current_page('LoginPage')
    username = page['username']
    password = page['password']
    loginbtn = page['loginbtn']
    login_page_activity = page["Activity"]

    def login_action(self, username, password):
        self.wait_activity(self.login_page_activity)
        self.type(self.username, username)
        self.type(self.password, password)
        self.clickat(self.loginbtn)


