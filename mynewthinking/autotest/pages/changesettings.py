# coding=utf-8
__author__ = 'Anderson'
import time

from autotest.Base import Base_page
from autotest.public.elementhelper import element_exist
from autotest.public.yamlmanage import YAML
from globals import PLATFORM, WAIT_TIME, WAIT_MAX_TIME, WAIT_MINI_TIME, WAIT_LONG_TIME
from autotest.public.content_helper import check_language_type


class Settings(Base_page):
    def __init__(self, driver):
        self.driver = driver

    course_page = YAML().current_page("CourseOverViewPage")
    unittitle = course_page['unittitle']

    setting = course_page['settings']
    settings_logout = course_page['logout']

    setting_page = YAML().current_page("SettingPage")
    language = setting_page['language']
    language_set = setting_page['languageset']
    language_back = setting_page['language_back']



    def change_language_android(self,language): # English,Español,Deutsch,Français,Italiano,简体中文
        time.sleep(WAIT_TIME)
        self.clickat(self.setting)
        time.sleep(WAIT_MINI_TIME)
        self.clickat(self.language)
        languageset = self.language_set%(language)
        print("language will changed for {}".format(languageset))
        self.clickelement(languageset)
        #self.clickat(self.language_back)
        time.sleep(WAIT_TIME)
        # text=self.getelementtext(self.unittitle)
        # assert(check_language_type(text,language))





