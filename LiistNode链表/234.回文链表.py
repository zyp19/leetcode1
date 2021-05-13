"""234. 回文链表
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
"""
def print_linklist(head):
    while head:
        print(head.val, end=',')
        head = head.next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_linklist_tail(self,li):
        head = ListNode(val = li[0])
        tail = head
        for _ in li[1:]:
            node = ListNode(val=_)
            tail.next = node
            tail =node
        return head
class Solution:
    # 复制输入的链表，也不知道干嘛，练练手不含头结点的尾插法
    def copyList(self, head):
        # 只有头指针的h
        tail = h =  ListNode(val = head.val)
        head = head.next
        while head:
            node = ListNode(head.val)
            tail.next = node
            tail = node
            head = head.next
        return h

    # 反转链表，使用头插法建立一个新的链表
    def isPalindrome(self,head):
#         建立一个单链表，存放给定链表的反转
        f = head
        h = ListNode(val = head.val)
        head = head.next
        while head:
            node = ListNode(head.val)
            node.next = h
            h = node
            head = head.next
        while h and f:
            if h.val == f.val:
                h = h.next
                f = f.next
            else:
                return False
        return True
    # 方法二 用栈的方法来做，为什么能想到栈的方法呢，原因是只要存链表中的值，如果是正序的情况，则可以存到一个数组中；如果是倒序的情况，则可以存到一个栈中，
    # 因为栈是后进先出的，正好是个倒序。
    # 用栈做题的另一个特点是相邻元素，对相邻元素进行删除或添加，就用栈！比如 1047. 删除字符串中的所有相邻重复项
    def stack_isPalindrome(self,head):
        stack = []
        h = head
        while head:
            stack.append(head.val)
            head = head.next
        while stack and h:
            tmp = stack.pop(-1)
            if tmp == h.val:
                h = h.next
            else:
                return False
        return True

solution = Solution()
li = [1,2]
list1 = ListNode()
list1=list1.create_linklist_tail(li)
result1 = solution.isPalindrome(list1)
result2 = solution.stack_isPlindrome(list1)
print(result1)
print(result2)
