# -*- coding: utf-8 -*-
# @Time	: 2021/2/23 19:08
# @Author	: xiaolan
# @File	: game_round1.py

#1、定义一个函数，回合制打架
import random


def fight(my_hp,my_power,enemy_hp,enemy_power):
    print(f"我的血量{my_hp},我的攻击力{my_power}")
    print(f"敌人的血量{enemy_hp}，敌人的攻击力{enemy_power}")

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        print(f"我的血量{my_hp}")
        print(f"敌人的血量{enemy_hp}")
        if my_hp <= 0:
            print("我输了")
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break
        elif my_hp == enemy_hp & my_hp<=0 & enemy_power :
            print("平局")
            break

if __name__ == "__main__":
    hp = [x for x in range(500,1000)]
    print(hp)
    fight(random.choice(hp),400,random.choice(hp),100)

