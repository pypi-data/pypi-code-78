# -*- coding:utf-8 -*-
from __future__ import unicode_literals
PARTY_STATUS_TEST = 0
PARTY_STATUS_USING = 1
PARTY_STATUS_GIVEUP = 2
PARTY_STATUS_STOP = 4
CHOICES_PARTY_STATUS = (
    (PARTY_STATUS_TEST, '测试中'),
    (PARTY_STATUS_USING, '正式使用'),
    (PARTY_STATUS_GIVEUP, '放弃'),
    (PARTY_STATUS_STOP, '停止使用')
)

APP_STATUS_UNINSTALL = 0
APP_STATUS_INSTALL = 1

CHOICES_APP_STATUS = (
    (APP_STATUS_UNINSTALL, "未安装"),
    (APP_STATUS_INSTALL, "已安装"),
)
