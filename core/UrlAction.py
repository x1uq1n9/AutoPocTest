# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

def UrlAction(url):
    if url[:4] == 'http':
        url = url
    else:
        url = 'http://' + url
    return url