"""
160.编写一个程序，找到两个单链表相交的起始节点。
"""
"""
思路还是快慢指针法，做了环形链表已经了解了快慢指针，但是居然还做不出来这道题。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        
