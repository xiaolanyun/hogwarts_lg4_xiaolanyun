# -*- coding: utf-8 -*-
# @Time	: 2021-04-14 20:44
# @Author	: xiaolan
# @File	: test_mem.py
from pageObject.page.index_page import IndexPage


class TestMem:
    def setup(self):
        self.index = IndexPage()
    def test_mem(self):
        name = 1
        addmempage = self.index.add_member()
        reslut = addmempage.get_member()
        assert name in reslut