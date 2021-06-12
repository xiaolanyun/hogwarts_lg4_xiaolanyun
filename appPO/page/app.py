# -*- coding: utf-8 -*-
# @Time	: 2021-05-13 17:21
# @Author	: xiaolan
# @File	: app.py
from appium import webdriver
from appPO.page.base_page import BasePage
from appPO.page.main import Main
class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity=".view.WelcomeActivityAlias"
        if self._driver is None:
            caps={}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermissions"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package,_activity)
        return self

    def main(self):
        return Main(self._driver)