# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9
import requests


def test(url):
    url = url + "/seeyon/htmlofficeservlet"
    info = requests.get(url, timeout=2).text
    if "htmloffice operate" in info:
        print(url + " Success! ")
    else:
        print(url + " False! ")