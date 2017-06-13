# coding=utf-8
__author__ = 'Anderson'
from autotest.Base import Base_page
from autotest.public.yamlmanage import YAML


class Login(Base_page):
    page = YAML().current_page('LoginPage')
    username = page['username']
    password = page['password']
    loginbtn = page['loginbtn']

    page_course = YAML().current_page('CourseOverViewPage')
    settings = page_course['settings']
    settings_logout = page_course['settings_logout']

    def login_action(self, username, password):
        self.type(self.username, username)
        self.type(self.password, password)
        self.clickat(self.loginbtn)

    def logout(self):
        self.clickat(self.settings)
        self.clickat(self.settings_logout)
