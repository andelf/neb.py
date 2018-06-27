# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Neb.py
# @Software: PyCharm
from nebpysdk.src.client.Api import Api
from nebpysdk.src.client.Admin import Admin


class Neb(object):


    # todo host_const

    def __init__(self, host="https://mainnet.nebulas.io", config={}):
        self.api = Api(host=host, config=config)
        self.admin = Admin(host=host, config=config)

    def set_request(self):
        self.api.set_request()
        self.admin.set_request()

