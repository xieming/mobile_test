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
    def to_id(product):
        return {
            Product.B2B: 2,
            Product.B2C: 1,
            Product.EC: 4
        }[product]

    @staticmethod
    def to_name_tablet(product):
        return {
            Product.B2C: 'englishtown',
            Product.B2B: 'corporate',
            Product.EC: 'englishcenters'
        }[product]


class Platform:
    ANDROID = 'Android'
    IOS = 'iOS'

JENKINS_HOST = "10.128.42.155:8080"