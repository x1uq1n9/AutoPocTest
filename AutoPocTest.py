# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

import lib.GetIp as GetIp
import lib.FofaApi as FofaApi
import lib.ShodanApi as ShodanApi
import core.FofaSpider as FofaSpider

# 查询语句
# query = '''致远A8+协同管理软件 V6.1'''
query = '''header="Ubuntu"'''

# FoFaApi开关以及配置
USE_FofaApi = False
FOFA_EMAIL = ""
FOFA_KEY = ""

# ShodanApi开关以及配置
USE_ShodanApi = True
Shodan_Api = ""

# 调用exp
FUNCTION = "seeyon_getshell.test(url)"
# FUNCTION = "thinkphp_view_recent_xff_sqli.thinkphp_view_recent_xff_sqli_verify(url)"

if __name__ == '__main__':
    FofaSpider.banner()
    if USE_FofaApi:
        FofaApi.FoFaApi_Action(query, FOFA_EMAIL, FOFA_KEY, FUNCTION)
    elif USE_ShodanApi:
        ShodanApi.ShodanApi_Action(query, Shodan_Api, FUNCTION)
    else:
        GetIp.action().IpAction(FUNCTION)