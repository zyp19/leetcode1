"""206. 反转链表（5.16没想起来 考察指数：*****）
反转一个单链表。
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
论坛思路：是一个链表从前往后更改链表指针域的指向 的操作！其实核心代码是删除头结点的操作
注意：1.头结点和头指针是不一样的
pre = ListNode(None)就是定义了一个头结点
pre = None是定义了一个头指针
2.指针 = 节点（在前面的表示指针，在后面的表示节点，意思是指针指向节点）**记住这个哈！！
"""
class Solution:
    # 原地反转链表
    def reverseList(self, head: ListNode):
        # pre = ListNode(None)
        pre = None
        cur = head
        while cur:
            # 避免丢失后面的链
            temp = cur.next
            # 删除头结点的操作是pre = cur.next
            cur.next = pre
            #后移pre cur
            pre = cur
            cur = temp
        return pre

"""
做不出来的原因分析：
我想的是走到尾结点处，把尾结点值赋给新链表，然后删掉尾结点，head是可以后移的（pre=head,head=head.next），但是pre不能前移
"""
# class Solution:
#     def reverseList(self, head: ListNode):
#         pre = head
#         h = ListNode(None)
#         node = h.next
#         # 删除尾结点
#         while pre != None:
#             while head.next != None:
#                 pre = head
#                 head = head.next
#             node = ListNode(head.val)
#             pre.next = None
#             head = pre
# 2021.6.22 ac
class Solution:
    def reverseList(self, head: ListNode):
        pre =  None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
