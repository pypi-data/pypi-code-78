# -*- coding: UTF-8 -*-
import random


def random_str(*args):
    """
    :param: *args 任意字符串组
    :return: str 随机字符串
    """
    choice = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    a = ''
    for arg in args:
        if arg is None:
            continue
        a += arg if type(arg) == str else str(arg)
    for i in range(8):
        a += random.choice(choice)
    print(a)
    return a


def random_phone():
    """
    :return: str 随机130开头的手机号
    """
    choice = '1234567890'
    a = '130'
    for i in range(8):
        a += random.choice(choice)
    return a


def random_email():
    """
    :return: str 随机oschina.cn结尾的邮箱号
    """
    choice = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    a = ''
    for i in range(8):
        a += random.choice(choice)
    return a + '@oschina.cn'


keyword = {
            'random_str': random_str,
            'random_phone': random_phone,
            'random_email': random_email}