# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9
from gevent import monkey

monkey.patch_all()
import base64
import requests
import json
from gevent.pool import Pool
import gevent
import GetPlugs


def FoFaApi_Action(query, FOFA_EMAIL, FOFA_KEY, FUNCTION):
    url_list = []
    qbase64 = str(base64.b64encode(query.encode()), encoding='utf-8')
    FOFA_URL = "https://fofa.so/api/v1/search/all?email={}&key={}&qbase64={}".format(FOFA_EMAIL, FOFA_KEY, qbase64)
    info = requests.get(url=FOFA_URL).text
    info_json = json.loads(info)
    ip_results = info_json['results']
    print("\033[32mTotal {} results\033[0m".format(len(ip_results)))
    for url_info in ip_results:
        url = url_info[0]
        if url[:4] == 'http':
            url = url
        else:
            url = 'http://' + url
        url_list.append(url)
    # print(url_list)

    pool = Pool(20)
    threads = [pool.spawn(GetPlugs.GetPlugs, ip, FUNCTION) for ip in url_list]
    gevent.joinall(threads)