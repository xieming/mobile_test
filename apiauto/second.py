import requests
import unittest

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

class DemoApi(object):
    def __init__(self,base_url):
        self.base_url=base_url
    def login(self,username,password):
        """登录接口
        :param username:用户名
        :param password:密码
        """
        url=urljoin(self.base_url,'login')
        data={'username':username,'password':password}
        return requests.post(url,data=data).json()

    def get_cookies(self,username,password):
        """
        获取登录cookies

        """
        url=urljoin(self.base_url,'login')
        data={'username':username,'password':password}
        return requests.post(url,data=data).cookies

    def info(self,cookies):
        """
        详情接口

        """
        url=urljoin(self.base_url,'info')
        return requests.get(url,cookies=cookies).json()

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url='http://127.0.0.1:5000'
        cls.username='admin'
        cls.password='123456'
        cls.app=DemoApi(cls.base_url)

    def test_login(self):
        """
        测试登录
        """
        response=self.app.login(self.username,self.password)
        assert response['code']==200
        assert response['msg']=='success'

    def test_info(self):
        """

        测试获取设备详情
        """
        cookies=self.app.get_cookies(self.username,self.password)
        response=self.app.info(cookies)
        assert response['code']==200
        assert response['msg']=='success'
        assert response['data']=='info'

if __name__ == "__main__":
    unittest.main()