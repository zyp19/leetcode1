#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/3/17

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# 头插法，每次把插入的节点放在最前面，因此得到的链表顺序和list的顺序是相反的
def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head
# 尾插法，得到的链表顺序和list的顺序相同
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head
# 遍历链表
def print_linklist(lk):
    while lk:
        print(lk.val, end=',')
        lk = lk.next

lk = create_linklist_head([1,2,3,6,8])
print_linklist(lk)