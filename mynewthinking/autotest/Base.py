__author__ = 'anderson'
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
import os, time


class Base_page():
    capabilities = {}
    capabilities['platformName'] = 'Android'
    capabilities['platformVersion'] = '5.1'
    capabilities['deviceName'] = "192.168.56.101:5555"
    capabilities['appPackage'] = 'com.ef.core.engage.englishtown'
    capabilities['appActivity'] = 'com.ef.core.engage.ui.screens.activity.EnglishTownSplashActivity'
    capabilities['appWaitActivity'] = 'com.ef.core.engage.ui.screens.activity.EnglishTownLoginActivity'
    capabilities['app'] = '/Users/anderson/Downloads/engage-englishtown-qa-debug-1.5.0-201705271211.apk'
    # capabilities['unicodeKeyboard'] = True
    capabilities['resetKeyboard'] = True
    capabilities['noSign'] = True
    capabilities['noReset'] = True

    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.capabilities)

    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

        # 重新封装一组元素定位方法

    def find_elements(self, loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

        # 	def typevalue(self,username,password):
        # 		webdriver.Remote.find_element_by_xpath(self,"//*[@resource-id='com.ef.core.engage.englishtown:id/txtName']").send_keys(username)
        # 		webdriver.Remote.find_element_by_xpath(self,"//*[@resource-id='com.ef.core.engage.englishtown:id/txtPwd']").send_keys(password)
        # 		webdriver.Remote.find_element_by_xpath(self,"//*[contains(@resource-id,'com.ef.core.engage.englishtown:id/btnLogin')]").click()
        # # #重新封装输入方法

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print("%s 页面未能找到 %s 元素" % (self, loc))

        # 重新封装按钮点击方法

    def clickButton(self, loc, find_first=True):
        try:
            if find_first:
                self.find_element(loc)
            self.find_element(loc).click()
        except AttributeError:
            print("%s 页面未能找到 %s 按钮" % (self, loc))

        # savePngName:生成图片的名称

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
