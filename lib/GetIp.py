# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9
from gevent import monkey

monkey.patch_all()
import requests
import time
from lxml import etree
import sys
from core.settings import UserAgent, cookie, query
from urllib.parse import quote
import base64
import gevent
import core.GetPlugs as GetPlugs
import core.FofaSpider as FofaSpider
from gevent.pool import Pool
import core.UrlAction as UrlAction


class action(object):

    def __init__(self):
        self.args = []
        self.source = None
        self.query = query
        self.spidernum = 0
        self.startpage = 1
        self.Cookie = cookie
        self.UserAgent = UserAgent
        self.q = quote(self.query)
        self.qbase64 = quote(str(base64.b64encode(self.query.encode()), encoding='utf-8'))

    def IpAction(self, FUNCTION):
        page, i, sheet, header = FofaSpider.FofaSpider.spider(self)
        try:
            pagenum = int(page) + 1
            for n in range(self.startpage, pagenum):
                if self.spidernum != 0 and (n == (self.startpage + self.spidernum + 1)):
                    break

                target = 'https://fofa.so/result?page={}&q={}&qbase64={}&full=true'.format(n, self.q, self.qbase64)
                res = requests.get(url=target, headers=header).text
                selector = etree.HTML(res)
                codes = "".join(selector.xpath('//*[@id="ajax_content"]/div/div[2]/div[2]/div/div[1]/text()'))  # 爬取状态码
                domain = selector.xpath('//*[@id="ajax_content"]/div/div[1]/div[1]/a/text()')  # 爬取域名或ip
                domain = [value.strip('\n').strip(' ') for value in domain if len(value.strip('\n').strip(' ')) != 0]
                # nums = compile.findall(codes)  # 状态码列表
                # res = zip(domain, nums)
                if len(domain) == 0:
                    sys.exit(0)
                # rdp等协议类查询
                if len(domain) == 0:
                    domain = selector.xpath('//*[@id="ajax_content"]/div/div/div[1]/div[1]/text()')
                    domain = [value.strip(' ').strip('\n').strip(' ') for value in domain]
                    print("\033[31m第%s页\033[0m" % str(n))
                    for value in domain:
                        print(value)
                        sheet.write(i, 0, value)
                        i += 1
                    time.sleep(1)

                else:
                    # 域名和ip聚合成字典
                    # res = zip(domain, nums)
                    res = zip(domain)
                    print("\033[31m第%s页\033[0m" % str(n))
                    url_list = []

                    for value in res:
                        try:
                            # print(str(i + 1) + ": " + value[0] + ": " + value[1])
                            url = value[0]
                            url = UrlAction.UrlAction(url)
                            url_list.append(url)
                            # 调用poc或exp
                            # GetPlugs.GetPlugs(url)

                            # sheet.write(i, 0, value[0])
                            # sheet.write(i, 1, value[1])
                            i += 1
                        except Exception as e:
                            print("\033[31m[!]异常！\033[0m")
                            print(e)
                            pass
                        # time.sleep(1)

                    pool = Pool(20)
                    threads = [pool.spawn(GetPlugs.GetPlugs, ip, FUNCTION) for ip in url_list]
                    gevent.joinall(threads)

                # 关闭写文件功能
                # filename.save('./{}.csv'.format(name))
            # sys.stdout.write('\033[31m搜集结果为{}.csv\n\n\033[0m'.format(name))

        except Exception as e:
            print("'\033[31m[!]异常退出！\033[0m'")
            print(e)
