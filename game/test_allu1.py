# -*- coding: utf-8 -*-
# @Time	: 2021/3/8 21:04
# @Author	: xiaolan
# @File	: test_allu1.py
import allure
import pytest
@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_sucess(self):
        print("登录用例：登陆成功")
        pass
    @allure.story("登录失败")
    def test_login_fail(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败")
        pass
if __name__ == '__main__':
    pytest.main()