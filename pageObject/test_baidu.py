# -*- coding: utf-8 -*-
# @Time	: 2021-03-30 20:59
# @Author	: xiaolan
# @File	: test_baidu.py
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class Testbaidu:
    def setup(self):
        self.driver = webdriver.Firefox(executable_path="E:\python3.8\geckodriver.exe")
        self.driver.get("https://www.baidu.com")
    def teardown(self):
        self.driver.quit()
    def test_baidu(self):
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹")
        # self.driver.find_element(By.CSS_SELECTOR, 'id=kw').send_keys("你好")
        # self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("你好")
        element_click = self.driver.find_element(By.CSS_SELECTOR,'#kw')
        element_doubleclick = self.driver.find_element(By.CSS_SELECTOR,'#kw')
        element_rightclick = self.driver.find_element_by_id('kw')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        action.perform()






























