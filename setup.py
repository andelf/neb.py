# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 下午5:18
# @Author  : GuoXiaoMin
# @File    : setup.py
# @Software: PyCharm

from setuptools import setup, find_packages

setup(
    name='NebulasSdkPy',
    version='0.3.0',
    author='GuoXiaoMin',
    packages=find_packages(exclude=["test", "test.*"]),
    url='',
    license='LICENSE.txt',
    description='NebulasSdkPy',
    #long_description=open('README.md').read(),
    install_requires=[
        "Crypto == 1.4.1",
        "eth-hash == 0.1.3",
        "eth-keyfile == 0.5.1",
        "eth-keys == 0.2.0b3",
        "eth-utils == 1.0.3",
        "protobuf == 3.5.2.post1",
        "pyscrypt == 1.6.2",
        "requests",
        "six",
    ],
)