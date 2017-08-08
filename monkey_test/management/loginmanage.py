from globals import WAIT_TIME

__author__ = 'anderson'
import time

from appium import webdriver

from management.yamlmanage import YAML
from globals import PLATFORM, AppPath, build_path


def login(device):
    capabilities = YAML().get_appium_config()

    if PLATFORM == 'Android':
        capabilities['app'] = AppPath.get_app_filename(build_path)
        capabilities['platformVersion'] = device["version"]
        capabilities['deviceName'] = device["name"]

        print(capabilities)

        driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        print(driver)
        time.sleep(WAIT_TIME)
        usernametxt = device["username"][0:device["username"].index('/')]
        passwordtxt = device["username"][device["username"].index('/')+1:]
        username = driver.find_element_by_id("txtName")
        username.clear()
        driver.set_value(username, usernametxt)
        password = driver.find_element_by_id("txtPwd")
        password.clear()
        driver.set_value(password, passwordtxt)
        driver.find_element_by_id("btnLogin").click()
        time.sleep(WAIT_TIME)
