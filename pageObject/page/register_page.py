# -*- coding: utf-8 -*-
# @Time	: 2021-04-14 16:35
# @Author	: xiaolan
# @File	: register_page.py
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def register(self):
        #注册页面填写信息
        self.driver.find_element(By.CSS_SELECTOR,"#corp_name").send_keys("c")
        return True
