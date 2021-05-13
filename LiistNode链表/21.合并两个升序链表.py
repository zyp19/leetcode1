"""将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        # 尾插法插入元素，定义一个h为头结点，head实际上为尾结点，插入过程保证head指向最后一个节点
        h = ListNode()
        head = h
        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        else:
            head.next = l2
        return h.next
solution = Solution()
l1 = ListNode([8,1,3])
l2 = ListNode([9,1,2])
h=solution.mergeTwoLists(l1, l2)
print(h.val)

