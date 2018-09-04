#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_login.py
@time: 17-4-19 上午10:41
"""
import unittest, requests
from lib.log import LOG
from lib.tools import failrun
from parameterized import parameterized, param


class TestSignUp(unittest.TestCase):
    '''报名接口测试'''

    def setUp(self):
        self.url = 'http://bj.tuanche.com/bentley/api/applyForTcjAsyn/'
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }

    @parameterized.expand(
        [
            param(data_params={'name': 'linlang9', 'cityId': 10, 'carStyleId': 32633, 'brandId': 67, 'groupbyType': 1,
                               'groupbyNum': 2001}),
            param(data_params={'name': 'linlang9', 'cityId': 10, 'carStyleId': 32633, 'brandId': 67, 'groupbyType': 1,
                               'groupbyNum': 2001}),
            param(
                data_params={'phone': '15633669988', 'cityId': 10, 'carStyleId': 32633, 'brandId': 67, 'groupbyType': 1,
                             'groupbyNum': 2001}),
            param(data_params={'name': 'linlang9', 'phone': '15633669988', 'carStyleId': 32633, 'brandId': 67,
                               'groupbyType': 1,
                               'groupbyNum': 2001})
        ]
    )
    def test_sign(self, data_params):
        '''报名'''
        data = data_params
        # name=linlang&=15601128781&cityId=10&carStyleId=32633&brandId=67&groupbyType=1&groupbyNum=2001
        response = requests.post(self.url, data=data)
        # self.assertEqual(response.status_code, 200, '断言状态码为200')
        print(response.text)
        self.assertEqual(response.json()['code'], 10000, '断言结果为10001')

    def tearDown(self):
        pass


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestSignUp("test_sign"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
