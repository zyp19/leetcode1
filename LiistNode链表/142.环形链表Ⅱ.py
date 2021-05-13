"""142.环形链表Ⅱ
给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。进阶：你是否可以使用 O(1) 空间解决此题？
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 第一次相遇
        fast,slow = head.next,head
        if head == None:
            return None
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         break
        # if not fast or not fast.next:
        #     return None
        while slow!=fast:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
        slow = head
        # 第二次相遇
        while fast!= slow:
            fast = fast.next
            slow = slow.next
        return slow