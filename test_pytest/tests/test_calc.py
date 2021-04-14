# -*- coding: utf-8 -*-
# @Time	: 2021/3/15 18:21
# @Author	: xiaolan
# @File	: test_calc.py
import pytest
from test_pytest.core.calc import Calc

@pytest.mark.parametrize('a,b,c',[
    [1,2,3]

])
def test_div(a,b,c):
    cla = Calc()
    assert cla.div(a,b) == c


def test_mul():
    assert False
