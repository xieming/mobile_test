__author__ = 'anderson'
import os
import time
import re

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from autotest.public.yamlmanage import YAML
from globals import WAIT_MAX_TIME,PLATFORM,AppPath,build_path
import inspect


#
# locator_to_by_map = {
#     "id": By.ID,
#     "xpath": By.XPATH,
#     "link": By.LINK_TEXT,
#     "partial_link": By.PARTIAL_LINK_TEXT,
#     "name": By.NAME,
#     "tag": By.TAG_NAME,
#     "class": By.CLASS_NAME,
#     "css": By.CSS_SELECTOR
# }


class Base_page():
    capabilities = YAML().current_device()
    if PLATFORM == 'Adroid':
        capabilities['app'] = AppPath.get_app_filename(build_path)

    print(capabilities)

    # capabilities['platformName'] = 'Android'
    # capabilities['platformVersion'] = '5.1'
    # capabilities['deviceName'] = "192.168.56.101:5555"
    # capabilities['appPackage'] = 'com.ef.core.engage.englishtown'
    # capabilities['appActivity'] = 'com.ef.core.engage.ui.screens.activity.EnglishTownSplashActivity'
    # capabilities['appWaitActivity'] = 'com.ef.core.engage.ui.screens.activity.EnglishTownLoginActivity'
    # capabilities['app'] = '/Users/anderson/Documents/builds/engage-englishtown-uat-debug-1.5.0.apk'
    # # capabilities['unicodeKeyboard'] = True
    # capabilities['resetKeyboard'] = True
    # capabilities['noSign'] = True
    # capabilities['noReset'] = True

    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.capabilities)

    # def locator_to_by_value(self,locator):
    #     separator_index = locator.find(";")
    #     by = locator[:separator_index]
    #     value = locator[separator_index + 1:]
    #     try:
    #         by = locator_to_by_map[by]
    #     except KeyError:
    #         print("The by <%s> of locator <%s> is not a valid By." % (by, locator))
    #     return by, value

    def action_element(self, by, value):

        if by == 'id':

            try:
                element = self.driver.find_element_by_id(value)
            except NoSuchElementException:
                return False

        if by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(value)
            except NoSuchElementException:
                return False

        if by == 'name':
            try:
                element = self.driver.find_element_by_name(value)
            except NoSuchElementException:
                return False

        return element

    def action_elements(self, by, value):
        elements = ""
        if by == 'id':
            elements = self.driver.find_elements_by_id(value)
        if by == 'xpath':
            elements = self.driver.find_elements_by_xpath(value)
        return elements

    def find_element(self, tag):
        key = tag.split(";")[0]
        value = tag.split(";")[1]
        if self.action_element(key, value):
            # WebDriverWait(self.driver, MAX_TIMES).until(self.action_element(key, value).is_displayed())
            return self.action_element(key, value)

        else:
            print("%s page cannot find %s %s" % (self, key, value))
            return False

    def find_elements(self, tag):
        key = tag.split(";")[0]
        value = tag.split(";")[1]
        try:
            # WebDriverWait(self.driver, MAX_TIMES).until(self.action_element(key, value).is_displayed())
            # if len(self.action_element(key, value)):
            return self.action_elements(key, value)
        except NoSuchElementException:
            print("%s page cannot find %s %s" % (self, key, value))
            return False

    # def find_element(self, tag):
    #
    #     loc = (self.locator_to_by_value(tag))
    #     try:
    #         WebDriverWait(self.driver, MAX_TIMES).until(lambda driver: driver.find_element(*loc).is_displayed())
    #         return self.driver.find_element(*loc)
    #     except:
    #         print("%s page cannot find element %s " % (self, loc))
    #
    # def find_elements(self, tag):
    #
    #     loc = (self.locator_to_by_value(tag))
    #     try:
    #         WebDriverWait(self.driver, MAX_TIMES).until(lambda driver: driver.find_elements(*loc).is_displayed())
    #         if len(self.driver.find_elements(*loc)):
    #             return self.driver.find_elements(*loc)
    #     except:
    #         print("%s page cannot find elements%s" % (self, loc))

    def type(self, element, value):
        ele = self.find_element(element)
        # ele.clear()
        return self.driver.set_value(ele, value)

    def clickat(self, element):
        return self.find_element(element).click()

    def savePngName(self, name):
        """
        name：自定义图片的名称
        """
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = "Result/" + day + "/image/" + day
        tm = self.saveTime()
        type = ".png"
        if os.path.exists(fp):
            filename = fp + "/" + tm + "_" + name + type

            # print "True"
            return filename
        else:
            os.makedirs(fp)
            filename = fp + "/" + tm + "_" + name + type

            # print "False"
            return filename

            # 获取系统当前时间

    def saveTime(self):
        """
        返回当前系统时间以括号中（2014-08-29-15_21_55）展示
        """
        return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

        # saveScreenshot:通过图片名称，进行截图保存

    def saveScreenshot(self, name):
        """
        快照截图
        name:图片名称
        """
        # 获取当前路径
        # print os.getcwd()
        image = self.driver.save_screenshot(self.savePngName(name))
        return image

    def wait_activity(self, activity, time=10):
        self.driver.wait_activity(activity, time)

    def is_element_exists(self, tag):
        if self.find_element(tag):
            return True
        else:
            return False

    # driver.swipe(start_x, start_y, end_x, end_y, duration)
    def swipe(self, direction, duration=500):
        window_size = self.driver.get_window_size()
        if (window_size and 'width' in window_size and \
                    window_size['width'] and window_size['width'] > 0 and \
                        'height' in window_size and \
                    window_size['height'] and window_size['height'] > 0):

            width = window_size['width']
            height = window_size['height']

            if direction == 'up':
                self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, duration)
            elif direction == 'down':
                self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, duration)
            elif direction == 'left':
                self.driver.swipe(width * 3 / 4, height / 2, width / 4, height / 2, duration)
            elif direction == 'right':
                self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, duration)
            else:
                return False

            return True
        else:
            assert False, 'Fail to obtain window size for swiping! {0}'.format(window_size)

    def equals_ignore_case(self,str1, str2):
        return re.match(re.escape(str1) + r'\Z', str2, re.I) is not None

    def locator_to_by_value(self, tag):
        key = tag.split(";")[0]
        value = tag.split(";")[1]


        mobile_by_properties = [member for member in inspect.getmembers(By) if member[0][:1] != '_']
        property_name = [member[0] for member in mobile_by_properties
                         if self.equals_ignore_case(member[1], key)][0]
        by = eval("By.{}".format(property_name))

        return (by, value)

    def wait(self, timeout=WAIT_MAX_TIME):
        return WebDriverWait(self.driver, timeout)

    def wait_until(self, method, message=None, timeout=WAIT_MAX_TIME):
        return self.wait(timeout).until(method, message)

    def wait_unitl_not(self, method, message=None, timeout=WAIT_MAX_TIME):
        return self.wait(timeout).until_not(method, message)

    def wait_for_visibility_of_element(self, element, timeout=WAIT_MAX_TIME):
        return self.wait_until(EC.visibility_of(element),
                               "Element {} is not visible".format(element), timeout=timeout)

    def wait_for_presence_of_element_located(self, tag, timeout=WAIT_MAX_TIME):
        locator_info = self.locator_to_by_value(tag)
        return self.wait_until(EC.presence_of_element_located(locator_info),
                               "Element locator (by: {0}, value: {1}) is not present"
                               .format(locator_info[0], locator_info[1]), timeout=timeout)

    def wait_for_visibility_of_element_located(self, tag, timeout=WAIT_MAX_TIME):
        locator_info = self.locator_to_by_value(tag)
        return self.wait_until(EC.visibility_of_element_located(locator_info),
                               "Element locator (by: {0}, value: {1}) is not visible"
                               .format(locator_info[0], locator_info[1]), timeout=timeout)

    def wait_for_invisibility_of_element_located(self, locator, timeout=WAIT_MAX_TIME):
        return self.wait_until(EC.invisibility_of_element_located(locator),
                               "Element with locator {} is still existed".format(locator), timeout=timeout)
