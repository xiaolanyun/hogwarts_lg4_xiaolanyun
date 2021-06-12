# -*- coding: utf-8 -*-
# @Time	: 2021-05-13 17:33
# @Author	: xiaolan
# @File	: main.py
from appPO.page.base_page import BasePage
from appPO.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)