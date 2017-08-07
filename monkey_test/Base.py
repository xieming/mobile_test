__author__ = 'anderson'
import os
import time
import re

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

from management.yamlmanage import YAML
from globals import PLATFORM,AppPath,build_path
import inspect
from management.devicesmanage import get_devices_info





class Base_page():
    capabilities = YAML().get_appium_config()



    def __init__(self,device):
        if PLATFORM == 'Android':
            self.capabilities['app'] = AppPath.get_app_filename(build_path)
            self.capabilities['platformVersion'] = device["version"]
            self.capabilities['deviceName'] = device["name"]

        print(self.capabilities)
        self.driver = webdriver.Remote('http://localhost:{}/wd/hub'.format(device["port"]), self.capabilities)

