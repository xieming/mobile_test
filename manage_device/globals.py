import configparser

CONFLUENCE_LOGIN_URL = "https://confluence.englishtown.com/login.action?os_destination=%2Findex.action&permissionViolation=true"

CONFLUENCE_DEVICE_TRACKING_URL = "https://confluence.englishtown.com/pages/viewpage.action?pageId=673644924"

MAX_DAY = 30

MAIL_HOST = "smtp.office365.com"
SMTP_PORT = 587

cf = configparser.ConfigParser()
cf.read("config.ini")
username = cf.get("user", "username")
password = cf.get("user", "password")

EMAIL_TEXT = """
Hi {},

You've borrowed the device {} from mobile team over {} days.
You known the resource was limited.
If you don't use it any more, please return it to mobile team.
If you still need it for work, please reply this email and let me know how long will you want to take.

Thanks a lot!

"""
