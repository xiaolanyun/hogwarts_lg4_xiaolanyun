
# -*- coding: utf-8 -*-
# @Time	: 2021-06-12 11:00
# @Author	: xiaolan
# @File	: demo1.py
class TestStockSelect:
    @classmethod
    def setup_calss(cls):
        cls.stock_select_page = MainPage().stock_select()
        cls.stock_select_page.clear_all()
