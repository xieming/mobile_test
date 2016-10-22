#coding=utf-8
__author__ = 'Anderson'
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By

import time,os


class Base:
	driver = None
	capabilities = {'platformName': 'Android',
					# 'platformVersion':'6.0',
					# 'deviceName':'Nexus 5X',
					'platformVersion': '5.0',
					'deviceName': "Samsung Galaxy S6 - 5.0.0 - API 21 - 1440x2560",
					'appPackage': 'com.ef.core.engage.englishtown',
					#'appActivity': 'com.ef.core.engage.ui.screens.activity.LoginActivity',
					'app': '/Users/anderson/Downloads/engage-englishtown-uat-debug-1.0.5-201607211530.apk',  # monitor must
					'unicodeKeyboard': True,
					'resetKeyboard': True}

	driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

	# def __init__(self,driver):
	# 	self.driver = driver

#重新封装单个元素定位方法
	def find_element(self,loc):
		try:
			WebDriverWait(self.driver,15).until(lambda driver:driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except:
			print u"%s 页面中未能找到 %s 元素" %(self,loc)

	def find_element_by_xpath(self,str):
		try:
			WebDriverWait(self.driver,15).until(lambda driver:driver.find_element(str).is_displayed())
			print "ok"
			return self.driver.find_element_by_xpath()
		except:
			print u"%s 页面中未能找到 %s 元素" %(self,str)


tt = Base()
tt.find_element_by_xpath("//android.widget.EditText[contains(@text,'Username')]")
