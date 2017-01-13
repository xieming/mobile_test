#coding=utf-8
__author__ = 'Anderson'
from appium import webdriver
from selenium.webdriver.common.by import By
import BasePage
from time import sleep
import threading


#driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.Base.capabilities)
class Login(BasePage.Base):
	def __init__(self):
		threading.thread.__init__(self)

	#username input
	#usr_input = (By.ID,"com.ef.core.engage.englishtown:id/txtName")
	usr_input =(By.XPATH, "//*[contains(@text,'Username')]")
	#password input
	pwd_input = (By.ID,"com.ef.core.engage.englishtown:id/txtPwd")

	#login button
	login_btn =(By.ID,"com.ef.core.engage.englishtown:id/btnLogin")



	#input username
	def input_username(self,username):
		self.send_keys(self.usr_input,username)

	#input username
	def input_password(self,password):
		self.send_keys(self.pwd_input,password)

	#click login
	def click_login_button(self):
		self.clickButton(self.login_btn)
		sleep(2)


#搜索/收藏
	def run(self, username,password):

		self.capabilities = { 'platformName':'Android',
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

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.capabilities)


		self.capabilities1 = { 'platformName':'Android',
						# 'platformVersion':'6.0',
						# 'deviceName':'Nexus 5X',
						 'platformVersion':'5.0',
						# 'deviceName':"Samsung Galaxy S6 - 5.0.0 - API 21 - 1440x2560",
						 'deviceName': '192.168.56.102:5555',
						 'udid': '192.168.56.102:5555',
						 'appPackage':'com.ef.core.engage.englishtown',
						 'appActivity':'com.ef.core.engage.ui.screens.activity.LoginActivity',
						 'app': '/Users/anderson/Downloads/engage-englishtown-live-release.apk',
						 'unicodeKeyboard':True,
						 'resetKeyboard':True}

		self.driver1 = webdriver.Remote('http://localhost:4725/wd/hub', self.capabilities1)

		try:
			thread1=Login(BasePage.Base.driver)
			thread2=Login(BasePage.Base.driver1)
			thread1.start()
			thread2.start()

			self.input_username(username)
			self.input_password(password)
			self.click_login_button()
			sleep(10)
		#Loging_page.find_element("com.ef.core.engage.englishtown:id/textView")
			self.saveScreenshot('login')
		except:
			print "Error: unable to start thread"

		#BasePage.Base.driver.quit()
