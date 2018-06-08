# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : Neb.py
# @Software: PyCharm
from nebpysdk.src.client.Api import Api
from nebpysdk.src.client.Admin import Admin


class Neb:


    # todo host_const

    def __init__(self, host="https://mainnet.nebulas.io"):
        self.api = Api(host=host)
        self.admin = Admin(host=host)

    def set_request(self):
        self.api.set_request()
        self.admin.set_request()

