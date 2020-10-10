# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

import os
import pkgutil
# import importlib

pkgpath = os.path.dirname(__file__) + "/../plugins"
pkgname = os.path.basename(pkgpath)
print("\033[36mSuccessfully load plugins: \033[0m")

# 动态加载poc或exp脚本
plug_list = []
for _, file, _ in pkgutil.iter_modules([pkgpath]):
    print(file)
    # __import__(pkgname + '.' + file)
    plug_list.append(file)
    exec("import " + pkgname + "." + file + " as " + file)
    # module_object = importlib.import_module(pkgname + '.' + file) # 将模块加载为对象


def GetPlugs(url, FUNCTION):
    try:
        exec(FUNCTION)
        # seeyon_getshell.test(url)
    except Exception as e:
        print("\033[31m[!]" + url + "异常！\033[0m")
        print(e)
        pass