import configparser
from .datastruct import AppInfo

cf = configparser.ConfigParser()
cf.read("config.ini")

current_app_info = AppInfo()
current_app_info.app_env = cf.options("test.env")
current_app_info.app_product = cf.options('test.product')
current_app_info.app_platform = cf.options('test.platform')
current_app_info.app_job = cf.options('test.job')
