# -*- coding: utf-8 -*-
# @Time	: 2021-04-14 15:54
# @Author	: xiaolan
# @File	: main_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.page.login_page import LoginPage
from pageObject.page.register_page import RegisterPage


class MainPage:
    #定义一下初始driver
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="E:\python3.8\geckodriver.exe")
        self.driver.get("https://work.weixin.qq.com/?from=1014309098")


    def goto_login(self):
        #click login
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        #进入登录页面
        return LoginPage(self.driver)

    def goto_register(self):
        #click register
        return RegisterPage(self.driver)


































