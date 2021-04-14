# -*- coding: utf-8 -*-
# @Time	: 2021-04-14 16:11
# @Author	: xiaolan
# @File	: login_page.py
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageObject.page.register_page import RegisterPage


class LoginPage:
    #接收并指定类型
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def scan(self):
        pass
    def goto_register(self):
        #点击注册
        self.driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()
        #返回注册页面
        return RegisterPage(self.driver)