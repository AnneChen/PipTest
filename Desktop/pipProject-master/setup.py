#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from setuptools import setup, find_packages

setup(
    name = "mytool",
    version = "0.1.0",
    keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
    description = "time and path tool",
    long_description = "time and path tool",
    license = "MIT Licence",

    url = "https://github.com/AnneChen/PipTest.git",
    author = "anne",
    author_email = "617091464@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['chardet']
)