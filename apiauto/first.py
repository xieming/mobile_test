import unittest

import requests


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_url = 'http://127.0.0.1:5000/login'
        cls.info_url = 'http://127.0.0.1:5000/info'
        cls.username = 'admin'
        cls.password = '123456'

    def test_login(self):
        """测试登录"""
        data = {'username': self.username, 'password': self.password}
        response = requests.post(self.login_url, data=data).json()
        assert response['code'] == 200
        assert response['msg'] == 'success'

    def test_info(self):
        """测试info接口"""
        data = {'username': self.username, 'password': self.password}
        response_cookies = requests.post(self.login_url, data=data).cookies
        session = response_cookies.get('session')
        assert session
        info_cookies = {'session': session}
        response = requests.get(self.info_url, cookies=info_cookies).json()
        assert response['code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'

if __name__ == "__main__":
    unittest.main()
