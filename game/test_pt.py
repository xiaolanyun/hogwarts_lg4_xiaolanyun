# -*- coding: utf-8 -*-
# @Time	: 2021/3/3 20:20
# @Author	: xiaolan
# @File	: test_pt.py
import pytest
import yaml


def func(x):
    return x+1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,2)
])
def test_answer(a,b):
    assert func(a) ==b

@pytest.mark.parametrize("a,b",yaml.safe_load(open("./data.yaml")))
def test_ans(a,b):
    assert func(a) ==b




@pytest.fixture()
def login():
    name = "jet"
    return name

class TestDemo:
    def test_a(self,login):
        print(f"a,name={login}")
    def test_b(self):
        print("b")
    def test_c(self,login):
        print(f"c,name={login}")
if __name__ == '__main__':
    pytest.main(['test_pt.py::TestDemo','-v'])