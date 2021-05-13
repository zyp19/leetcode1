#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/4/14
# 分数背包问题
goods = [(60, 10),(100, 20),(120, 30)]  # 每个商品元组表示(价格, 重量)
# lambda是匿名函数，指一类无需函数名的函数或子程序，其中lambda后面的变量的含义是传参，冒号后面的是函数体的内容
# 传参可以有多个，但是函数体的表达式只能有一个
# lambda匿名函数的格式：冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。其实lambda返回值是一个函数的地址，也就是函数对象。
goods.sort(key=lambda x: x[0]/x[1], reverse=True)


def fractional_backpack(goods, w):
    # m是一个列表记录拿走物品的数量，m[i]为1（表示该物品全部都拿）或一个分数（只拿部分）
    m = [0 for _ in range(len(goods))]
    # 拿走物品的总价值
    total_v = 0
    # i是序号，(prize,weight)
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            # m[i]的意义是该物品的全部都拿进来
            m[i] = 1
            # 该物品都拿进来的话，总价值增加
            total_v += prize
            # 能装的余地就少了这么多
            w -= weight
        else:
            # m[i]的意义是拿一个商品的部分
            m[i] = w / weight
            # 该物品那劲一部分
            total_v += m[i] * prize
            # 既然走了else循环，说明该物品只能拿一部分，而且此时背包没有空余的地方了，所以w为0
            w = 0
            # 既然走了else循环，说明此时背包没有空余的地方了，那么下一次大for循环也没必要再进行了，所以直接break跳出大循环即可
            break
    return total_v, m

print(fractional_backpack(goods, 50))