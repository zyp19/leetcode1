"""203. 移除链表元素
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int):
        h = head
        pre = None
        # 一定要审题，注意一定要循环完整个链表才行
        while h:
            if h.val == val:
                temp = h.next
                if head == h:
                    head = h.next
                else:
                    pre.next = h.next
                h = temp
            else:
                pre = h
                h = h.next
        return head
solution =Solution()
H=solution.deleteNode(ListNode(1))