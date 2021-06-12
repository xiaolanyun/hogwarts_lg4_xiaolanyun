# -*- coding: utf-8 -*-
# @Time	: 2021-04-14 19:44
# @Author	: xiaolan
# @File	: index_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pageObject.page.addmember_page import AddMemberPage
from pageObject.page.base_page import BasePage
class IndexPage(BasePage):
    # def __init__(self):
    #     option = Options()
    #     option.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def add_member(self):
        self.find(By.CSS_SELECTER,".index_service_cnt_itemWrap:neth-child(1)")
        return AddMemberPage(self.driver)
