"""876.链表的中间节点
给定一个头结点为 head 的非空单链表，返回链表的中间结点。如果有两个中间结点，则返回第二个中间结点。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow