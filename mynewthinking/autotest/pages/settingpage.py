# coding=utf-8
__author__ = 'Anderson'
import time

from autotest.Base import Base_page
from autotest.public.elementhelper import element_exist
from autotest.public.yamlmanage import YAML
from globals import PLATFORM,WAIT_TIME,WAIT_MAX_TIME



class Setting(Base_page):
    def __init__(self,driver):
        self.driver=driver

    setting_page = YAML().current_page("SettingPage")
    language=setting_page['language']
    sync=setting_page['sync']
    logout=setting_page['logout']

    def change_language(self,language):
        pass



    def trigger_sync(self):
        self.clickelement(self.sync)
        time.sleep(WAIT_TIME)

    def log_out(self):
        pass

