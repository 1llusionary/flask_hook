# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 15:03
# @Author  : Zcs
# @File    : test_g.py
from flask import g


#  g: 处理请求时用作临时存储的对象。每次请求都会重设这个变量
def test_g():
    print('********')
    print(g.conn)
    print('********')
    return 0
