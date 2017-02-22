class Env:
    UAT_DEV = 'uat_dev'
    UAT_FIRST = 'uat_first'
    QA = 'qa'
    QACN = 'qacn'
    STG = 'stg'
    STGCN = 'stgcn'
    LIVE = 'live'
    LIVECN = 'livecn'

class Product:
    B2B = 'b2b'
    B2C = 'b2c'
    EC = 'ec'

    @staticmethod
    def to_package(product):
        return {
            Product.B2B: "com.ef.core.engage.corporate",
            Product.B2C: "com.ef.core.engage.englishtown",
            Product.EC: "com.ef.core.engage.smartenglish"
        }[product]

    @staticmethod
    def to_start_page(product):
        return {
            Product.B2B: "com.ef.core.engage.corporate/com.ef.core.engage.ui.screens.activity.CorporateLoginActivity",
            Product.B2C: "com.ef.core.engage.englishtown/com.ef.core.engage.ui.screens.activity.EnglishTownLoginActivity",
            Product.EC: "com.ef.core.engage.smartenglish/com.ef.core.engage.ui.screens.activity.SmartEnglishLoginActivity"
        }[product]

    @staticmethod
    def to_name(product):
        return {
            Product.B2C: 'englishtown',
            Product.B2B: 'corporate',
            Product.EC: 'smartenglish'
        }[product]


class Platform:
    ANDROID = 'Android'
    IOS = 'iOS'

JENKINS_HOST = "10.128.42.155:8080"