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
from lib.config_operate import ConfigOperate
from parameterized import parameterized, param


class TestPcSignUp(unittest.TestCase):
    '''报名接口测试'''

    def setUp(self):
        self.url = ConfigOperate('UrlConf').get_config('bj_tuanche', 'url')
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type":"application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }

    @parameterized.expand(
        [   param("all_null",
                  data_params={}),

            param("phone_null",
                  data_params={'username': 'zhangsan', 'password': '294b7d0de47943d8ef307a9636325331', 'token': 'c81a7765c623dd22263bfdacbbd55428', 
                  'type': 'ipk'}),
        ]
    )
    def test_sign_params_null(self, _, data_params):
        '''验证报名各字段参数为空'''
        uri = '/user/login'
        response = requests.post(self.url + uri, data=data_params, headers=self.headers)
        LOG.info('请求{0},参数{1},状态{2},\n 响应数据{3}'.format(uri, data_params, response, response.text))
        self.assertEqual(response.status_code, 200, '断言响应结果为200')
        self.assertEqual(response.json()['code'], 0, '断言结果为1')
        self.assertEqual(response.json()['msg'], '', '断言参数异常')

    

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()

