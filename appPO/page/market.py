# -*- coding: utf-8 -*-
# @Time	: 2021-05-14 10:42
# @Author	: xiaolan
# @File	: market.py
from appPO.page.base_page import BasePage
from appPO.page.search import Search
class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)