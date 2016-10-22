#coding=utf-8
__author__ = 'Anderson'
from appium import webdriver
from selenium.webdriver.common.by import By
import BasePage
from time import sleep


#driver = webdriver.Remote('http://localhost:4723/wd/hub', BasePage.Base.capabilities)
class Login(BasePage.Base):

	#username input
	#usr_input = (By.ID,"com.ef.core.engage.englishtown:id/txtName")
	usr_input =(By.XPATH, "//android.widget.EditText[contains(@text,'Username')]")
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
def login_action(username,password):
	Loging_page = Login(BasePage.Base.driver)
	Loging_page.input_username(username)
	Loging_page.input_password(password)
	Loging_page.click_login_button()
	sleep(10)
	#Loging_page.find_element("com.ef.core.engage.englishtown:id/textView")
	Loging_page.saveScreenshot('login')
	#BasePage.Base.driver.quit()
