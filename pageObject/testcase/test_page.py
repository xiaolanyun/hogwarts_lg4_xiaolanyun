# -*- coding: utf-8 -*-
# @Time	: 2021-04-14 19:25
# @Author	: xiaolan
# @File	: test_page.py
from pageObject.page.main_page import MainPage


class TestPage:
    def setup(self):
        self.main = MainPage()
    def test_register(self):
        result = self.main.goto_login().goto_register()
        assert result