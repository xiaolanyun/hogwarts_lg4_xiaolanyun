# -*- coding: utf-8 -*-
# @Time	: 2021/3/8 19:12
# @Author	: xiaolan
# @File	: test_pt1.py
import pytest
import yaml
class TestDe:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./data.yaml")))
    def test_an(self,env):
        if "test" in env:
            #["test:1.1.1.1"]
            print("测试环境")
            print(env)
            # print(env['test'])
        elif "dev" in env:
            print("这是开发环境")
    def test_yaml(self):
        print(yaml.safe_load(open("./data.yaml")))