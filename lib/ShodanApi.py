# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

from gevent import monkey

monkey.patch_all()
import shodan
from gevent.pool import Pool
import gevent
import core.GetPlugs as GetPlugs
import core.UrlAction as UrlAction


def ShodanApi_Action(query, Shodan_Api, FUNCTION):
    url_list = []
    api = shodan.Shodan(Shodan_Api)
    results = api.search(query)
    total = results['total']
    print("\033[32mTotal {} results\033[0m".format(total))
    for result in results['matches']:
        ip_str = result['ip_str']
        port = str(result['port'])
        # print(ip_str + ':' + port)
        url = ip_str + ":" + port
        url = UrlAction.UrlAction(url)
        url_list.append(url)

    pool = Pool(20)
    threads = [pool.spawn(GetPlugs.GetPlugs, ip, FUNCTION) for ip in url_list]
    gevent.joinall(threads)
