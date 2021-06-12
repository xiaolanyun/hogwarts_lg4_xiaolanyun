# -*- coding: utf-8 -*-
# @Time	: 2021-05-17 22:08
# @Author	: xiaolan
# @File	: test_appweb.py
from time import sleep
import pytest
from appium import webdriver


class TestappWeb:
    def setup(self):
        des_caps = {
            'platformName' : 'android',
            'platformVersion' : '6.0',
            'browserName' : 'Chrome',
            'noReset' : True,
            'deviceName' : '127.0.0.1:7555'
            'chromedriverExecutable' 'C:/Program Files/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/chromedriver76.exe'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(7)
    def teardown(self):
        self.driver.quit()
    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)