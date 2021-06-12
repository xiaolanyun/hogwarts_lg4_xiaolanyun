# -*- coding: utf-8 -*-
# @Time	: 2021-05-06 16:16
# @Author	: xiaolan
# @File	: test_xueqiu.py
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import unittest
from hamcrest import *


class TestXueqiu:
    def setup(self):
        describle_cap = {}
        describle_cap['platformName'] = 'Android'
        describle_cap['deviceName'] = '127.0.0.1:7555'
        describle_cap['appPackage'] = 'com.xueqiu.android'
        describle_cap['appActivity'] = '.view.WelcomeActivityAlias'
        describle_cap['noReset'] = 'true'
        # describle_cap['dontStopAppOnReset'] = 'True'
        describle_cap['unicodeKeyboard'] = 'true'
        describle_cap['resetKeyboard'] = 'true'
        describle_cap['skipDeviceInitialization'] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", describle_cap)
        self.driver.implicitly_wait(50)

    def taerdown(self):
        pass
        # self.driver.quit()

    # noReset操作应用后数据不清除
    def test_xue(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        el2 = WebDriverWait(self.driver, 5, 0.5).until(
            expected_conditions.visibility_of_element_located((MobileBy.ID, "cm.xueqiu.android:id/search_input_text")))
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        # el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
        el3.click()

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 0.8)
        y_end = int(height * 0.2)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        self.driver.set_network_connection()

#     def test_hamcrest(self):
# # assert_that(预期值, equal_to(实际值)， ‘抛出异常的提示信息’)
#         assert_that(10, equal_to(10))
#         # assert_that(预期值, close_to(实际值, 上下浮动值), '抛出异常提示信息')
#         assert_that(10, close_to(12, 2))
#         assert_that("some string", contains_string("string"))

    @pytest.mark.parametrize('searchkey, type, price', [
        ('alibaba', 'BABA', 210),
        ('xiaomi', '01810', 25)
    ])
    def test_search(self,searchkey, type, price):
        '''
        1、打开雪球应用
        2、点击搜索框
        3、输入 搜索词 ‘alibaba’  or  'xiaomi'
        4、点击第一个搜索结果
        5、判断  股票价格
        :return:
        '''
        search_element = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search")
        search_element.click()
        search_element2 = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text")
        search_element2.send_keys(searchkey)
        result1 = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name")
        result1.click()
        current_price = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"这是价格{current_price}")
        assert_that(float(current_price),close_to(price,price*0.1))




if __name__ == '__main__':
    pytest.main()
