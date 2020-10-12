# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

import re
import xlwt
import base64
import random
import requests

from datetime import datetime
from urllib.parse import quote
from core.settings import UserAgent, cookie


class FofaSpider(object):

    # query 就是我们的查询语句
    def __init__(self, query, startpage, spidernum):
        self.q = quote(query)
        self.qbase64 = quote(str(base64.b64encode(query.encode()), encoding='utf-8'))
        self.UserAgent = UserAgent
        # 这里的cookie 后面改成input 用户自己输入
        self.Cookie = cookie
        self.page = 1
        self.startpage = startpage
        self.spidernum = spidernum

    def spider(self):
        global i
        i = 0
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("\033[35mCurrent Time: " + now_time + "\033[0m")
        # 提取状态码
        # compile = re.compile('HTTP/1.1 (\d+) ')
        filename = xlwt.Workbook()
        sheet = filename.add_sheet('result')
        header = {"User-Agent": random.choice(self.UserAgent), "Cookie": self.Cookie}
        url = 'https://fofa.so/result?q={}&qbase64={}&full=true'.format(self.q, self.qbase64)
        html = requests.get(url=url, headers=header).text
        # print(html)
        pages = re.findall('>(\d*)</a> <a class="next_page" rel="next"', html)
        if len(pages) == 0:
            page = 1
        else:
            page = pages[0]

        print("\033[31m总共有{}页\033[0m".format(page))
        print("\033[31m查询语句为{}\033[0m".format(self.q))
        return page, i, sheet, header

    def run(self):
        self.spider()


def banner():
    print("""\033[33m
██╗  ██╗ ██╗██╗   ██╗         ██████╗  ██╗███╗   ██╗ █████╗ 
╚██╗██╔╝███║██║   ██║        ██╔═══██╗███║████╗  ██║██╔══██╗
 ╚███╔╝ ╚██║██║   ██║        ██║   ██║╚██║██╔██╗ ██║╚██████║
 ██╔██╗  ██║██║   ██║        ██║▄▄ ██║ ██║██║╚██╗██║ ╚═══██║
██╔╝ ██╗ ██║╚██████╔╝███████╗╚██████╔╝ ██║██║ ╚████║ █████╔╝
╚═╝  ╚═╝ ╚═╝ ╚═════╝ ╚══════╝ ╚══▀▀═╝  ╚═╝╚═╝  ╚═══╝ ╚════╝ \033[0m
    """)
