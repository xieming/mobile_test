from ptest import config
from enumeration import *
from datastruct import AppInfo

current_app_info = AppInfo()
current_app_info.app_env =config.get_property('test.env', default="uat").lower()
current_app_info.app_product = config.get_property('test.product',default=Product.B2C).lower()
current_app_info.app_platform = config.get_property('test.platform')
current_app_info.app_job = config.get_property('test.job',default="engage-android-snapshot")
current_app_info.app_type = config.get_property('test.type',default="debug")