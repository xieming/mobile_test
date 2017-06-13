__author__ = 'anderson'
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
import os, time
from selenium.webdriver.common.by import By
from globals import MAX_TIMES
from autotest.public.yamlmanage import YAML
from selenium.common.exceptions import NoSuchElementException




class Base_page():
    capabilities = YAML().current_device()
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

    # def actions(self,current,value):
    #     ele=""
    #     if current == 'id':
    #         ele=self.driver.find_element_by_id(value)
    #     if current == 'xpath':
    #         ele=self.driver.find_element_by_xpath(value)
    #     return ele


    # def find_element(self, tag):
    #     key = tag.split(";")[0]
    #     print(key)
    #     value = tag.split(";")[1]
    #
    #     by = eval("MobileBy.{}".format(key))
    #
    #     loc = (by, value)
    #
    #     # element=("MobileBy.{}".format(key),value)
    #
    #     try:
    #         WebDriverWait(self.driver,15).until(self.actions(key,value).is_displayed())
    #         return self.actions(key,value)
    #
    #         # WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*element).is_displayed())
    #         # return self.driver.find_element(by=element[0],value=element[1])
    #     except:
    #         print("%s page cannot find %s %s" % (self, key,value))

    def find_element(self, tag):
        key = tag.split(";")[0]
        value = tag.split(";")[1]
        by = eval("By.{}".format(key.upper()))
        loc = (by,value)
        try:
            WebDriverWait(self.driver, MAX_TIMES).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("%s page cannot find element %s " % (self, loc))

    def find_elements(self, tag):
        key = tag.split(";")[0]
        value = tag.split(";")[1]
        by = eval("By.{}".format(key.upper()))
        loc = (by, value)
        try:
            WebDriverWait(self.driver, MAX_TIMES).until(lambda driver: driver.find_elements(*loc).is_displayed())
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            print("%s page cannot find elements%s" % (self, loc))

    def type(self,element,value):
        ele = self.find_element(element)
        ele.clear()
        return self.driver.set_value(ele,value)

    def clickat(self,element):
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

    def wait_activity(self,activity,time=10):
        self.driver.wait_activity(activity,time)
        time.sleep(time)

    def is_element_exists(self,tag):
        try:
            self.driver.find_element(tag)
        except NoSuchElementException:
            return False
        return True


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
