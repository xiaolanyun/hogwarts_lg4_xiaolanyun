# -*- coding: utf-8 -*-
# @Time	: 2021/2/23 21:00
# @Author	: xiaolan
# @File	: cir.py
#定义一个自行车类
class bicycle:

    def run(self,km):
        print(f"脚骑了{km}")

class ebicycle(bicycle):
    def __init__(self,valume):
        self.valume = valume
    def fill_charge(self,vol):
        self.valume = vol + self.valume
        print(f"冲了{vol},充完电后是{self.valume}")
    def run(self,km):
        #获取目前电量最大里程
        power_km = self.valume * 10
        if power_km >= km:
            print(f"电量可以全部骑完{km}")
        else:
            #电量不够
            print(f"我电量骑行{power_km}")
            #非继承方式
            # bike = bicycle()
            # bike.run(km-power_km)
            #继承调用
            super().run(km-power_km)

ebike = ebicycle(10)
ebike.run(1000)