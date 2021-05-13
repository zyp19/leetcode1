#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/4/14
"""
有n个⾮负整数，将其按照字符串拼接的⽅式拼接为⼀个整数。 如何拼接可以使得得到的整数最⼤？
例：32,94,128,1286,6,71可以拼接除的最⼤整数为94716321286128
"""
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]

def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def number_join(li):
    # 数字转字符串li:['32', '94', '128', '1286', '6', '71']
    li = list(map(str, li))
    # 对key进行排序，key是什么样的值呢？是将x,y传入xy_cmp函数进行拼接后得到的值
    li.sort(key=cmp_to_key(xy_cmp))
    # 返回没有”“的li列表
    return "".join(li)

print(number_join(li))
