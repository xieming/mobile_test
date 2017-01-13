#coding=utf-8
__author__ = 'Anderson'
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

import time,os
import Queue
import threading

class Base(threading.Thread):
	# driver = None
	# capabilities = { 'platformName':'Android',
	# 				# 'platformVersion':'6.0',
	# 				# 'deviceName':'Nexus 5X',
	# 				 'platformVersion':'5.1',
	# 				# 'deviceName':"Samsung Galaxy S6 - 5.0.0 - API 21 - 1440x2560",
	# 				 'deviceName': '192.168.56.101:5555',
	# 				 'udid': '192.168.56.101:5555',
	# 				 'appPackage':'com.ef.core.engage.englishtown',
	# 				 'appActivity':'com.ef.core.engage.ui.screens.activity.LoginActivity',
	# 				 'app': '/Users/anderson/Downloads/engage-englishtown-live-release.apk',
	# 				 'unicodeKeyboard':True,
	# 				 'resetKeyboard':True}
    #
	# driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
    #
    #
	# capabilities1 = { 'platformName':'Android',
	# 				# 'platformVersion':'6.0',
	# 				# 'deviceName':'Nexus 5X',
	# 				 'platformVersion':'5.0',
	# 				# 'deviceName':"Samsung Galaxy S6 - 5.0.0 - API 21 - 1440x2560",
	# 				 'deviceName': '192.168.56.102:5555',
	# 				 'udid': '192.168.56.102:5555',
	# 				 'appPackage':'com.ef.core.engage.englishtown',
	# 				 'appActivity':'com.ef.core.engage.ui.screens.activity.LoginActivity',
	# 				 'app': '/Users/anderson/Downloads/engage-englishtown-live-release.apk',
	# 				 'unicodeKeyboard':True,
	# 				 'resetKeyboard':True}
    #
	# driver = webdriver.Remote('http://localhost:4725/wd/hub', capabilities1)
	def __init__(self,appium_driver):
		threading.Thread.__init__(self)
		self.capabilities={ 'platformName':'Android',
					# 'platformVersion':'6.0',
					# 'deviceName':'Nexus 5X',
					 'platformVersion':'5.1',
					# 'deviceName':"Samsung Galaxy S6 - 5.0.0 - API 21 - 1440x2560",
					 'deviceName': '192.168.56.101:5555',
					 'udid': '192.168.56.101:5555',
					 'appPackage':'com.ef.core.engage.englishtown',
					 'appActivity':'com.ef.core.engage.ui.screens.activity.LoginActivity',
					 'app': '/Users/anderson/Downloads/engage-englishtown-live-release.apk',
					 'unicodeKeyboard':True,
					 'resetKeyboard':True}

		self.driver = webdriver.Remote('http://localhost:4725/wd/hub', self.capabilities)

		def run(self):
			while not exit_flag:


#重新封装单个元素定位方法
	def find_element(self,loc):
		try:
			WebDriverWait(self.driver,15).until(lambda driver:driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except:
			print u"%s 页面中未能找到 %s 元素" %(self,loc)

#重新封装一组元素定位方法
	def find_elements(self,loc):
		try:
			if len(self.driver.find_elements(*loc)):
				return self.driver.find_elements(*loc)
		except:
			print u"%s 页面中未能找到 %s 元素" %(self,loc)

#重新封装输入方法
	def send_keys(self,loc,value,clear_first=True,click_first=True):
		try:
			if click_first:
				self.find_element(loc).click()
			if clear_first:
				self.find_element(loc).clear()
			self.find_element(loc).send_keys(value)
		except AttributeError:
			print "%s 页面未能找到 %s 元素" %(self,loc)

#重新封装按钮点击方法
	def clickButton(self,loc,find_first=True):
		try:
			if find_first:
				self.find_element(loc)
			self.find_element(loc).click()
		except AttributeError:
			print "%s 页面未能找到 %s 按钮" %(self,loc)

	#savePngName:生成图片的名称
	def savePngName(self, name):
		"""
		name：自定义图片的名称
		"""
		day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
		fp = "Result/" + day + "/image/" + day
		tm = self.saveTime()
		type = ".png"
		if os.path.exists(fp):
			filename = fp+"/" + tm+"_"+name+type
			print filename
			#print "True"
			return filename
		else:
			os.makedirs(fp)
			filename = fp+"/" + tm+"_"+name+type
			print filename
			#print "False"
			return filename

	#获取系统当前时间
	def saveTime(self):
		"""
		返回当前系统时间以括号中（2014-08-29-15_21_55）展示
		"""
		return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

	#saveScreenshot:通过图片名称，进行截图保存
	def saveScreenshot(self,name):
		"""
		快照截图
		name:图片名称
		"""
		#获取当前路径
		#print os.getcwd()
		image = self.driver.save_screenshot(self.savePngName(name))
		return image
