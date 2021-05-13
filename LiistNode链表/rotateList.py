"""
旋转链表：给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
k = 0,1,2...
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
k % length(listNode) == k(得到的链表是一样的)，即移动k % length(listNode)个位置
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def length(self, head):
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        return count
    def rotateList(self, head: ListNode, k: int):
        h = ListNode(next = head)
        pre = h
        j = h
        i = 0
        len = self.length(head)
        if len == 0:
            return None
        if len == 1:
            return head
        else:
            if k == 0 or k % len == 0:
                return head
            if k > 0 and k % len != 0:
                while i < len - k % len:
                    i += 1
                    j = j.next
                temp1 = j.next
                temp = temp1
                while temp1.next:
                    temp1 = temp1.next
                temp1.next  = pre.next
                pre.next = temp
                j.next = None
                return pre.next
solution = Solution()
# a = solution.length(ListNode([1,5,4,3,2]))
# print(a)
h1 = ListNode(1 ,ListNode(2 ,ListNode(3 ,ListNode(4 ,ListNode(5)))))
a = solution.length(h1)
print(a)
h2 = solution.rotateList(h1,10)
print(h2)






