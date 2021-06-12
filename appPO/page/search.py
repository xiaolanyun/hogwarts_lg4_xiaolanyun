# -*- coding: utf-8 -*-
# @Time	: 2021-05-14 10:46
# @Author	: xiaolan
# @File	: search.py
from appPO.page.base_page import BasePage
class Search(BasePage):
    def search(self,value):
        self._params["value"]=value
        self.steps("../page/search.yaml")
