# -*- coding: utf-8 -*-
# @Time	: 2021-04-14 20:01
# @Author	: xiaolan
# @File	: addmember_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pageObject.page.base_page import BasePage
class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver
    def add_mem(self):
        # self.driver.find_element(By.CSS_SELECTOR,"")
        pass
    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        # titles = []
        # for element in elements:
        #     titles.append(element.get_attribute("title"))
        titles = [element.get_attribute("title") for element in elements]
