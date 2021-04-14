# -*- coding: utf-8 -*-
# @Time	: 2021/3/8 20:05
# @Author	: xiaolan
# @File	: test_allu.py
import pytest
import allure
def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')