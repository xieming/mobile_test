#coding=utf-8
__author__ = 'Anderson'
from appium import webdriver
from selenium.webdriver.common.by import By
import BasePage
from time import sleep



class Level(BasePage.Base):

	download_btn = (By.ID,"com.ef.core.engage.englishtown:id/download_progress_bar")

	setting_btn = (By.CLASS_NAME,"android.widget.ImageButton")


	set_lang_btn =(By.ID,"android.widget.ImageButton")




#搜索/收藏
def download_action():
	Level_page = Level(BasePage.Base.driver)
	Level_page.clickButton(Level_page.download_btn)
	Level_page.clickButton(Level_page.setting_btn)
