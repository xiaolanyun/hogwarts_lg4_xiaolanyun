# -*- coding: utf-8 -*-
# @Time	: 2021-05-14 10:55
# @Author	: xiaolan
# @File	: test_search.py
from appPO.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")