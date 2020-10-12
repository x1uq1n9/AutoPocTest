# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

import lib.GetIp as GetIp
import lib.FofaApi as FofaApi
import lib.ShodanApi as ShodanApi
import core.FofaSpider as FofaSpider
import core.ConfRead as ConfRead

query = ConfRead.query
USE_FofaApi = ConfRead.USE_FofaApi
FOFA_EMAIL = ConfRead.FOFA_EMAIL
FOFA_KEY = ConfRead.FOFA_KEY
USE_ShodanApi = ConfRead.USE_ShodanApi
Shodan_Api = ConfRead.Shodan_Api
FUNCTION = ConfRead.FUNCTION

if __name__ == '__main__':
    FofaSpider.banner()
    if USE_FofaApi:
        FofaApi.FoFaApi_Action(query, FOFA_EMAIL, FOFA_KEY, FUNCTION)
    elif USE_ShodanApi:
        ShodanApi.ShodanApi_Action(query, Shodan_Api, FUNCTION)
    else:
        GetIp.action().IpAction(FUNCTION)