"""19.删除链表的倒数第N个节点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
"""
# 1.关键点是找倒数第n个节点的前驱
# 2.dummyNode（傻节点），链表常用技巧，用一个自造结点指向头结点，来避免删除头结点时对头结点的特殊讨论；
# 方法1：在head前面设置一个节点，遍历链表，找到第n-1个节点,倒数第n个节点的前驱是length - n-1 (5-2-1=2)
# 方法2：使用栈后入先出的性质，倒数第N个节点相当于第N个出栈的节点，将n个节点都出栈，那么栈顶就是第n-1个节点（第n个节点的前驱）
# 方法3：快慢指针：
# 本题就是很正常的双指针，需要注意的是，（找到被删除节点的前驱结点）比（找到被删除节点）更有价值。
# 双指针本质上和遍历两次在复杂度上并没有什么区别吧，无非是把两个串行的循环并行起来跑了，为什么被官方钦定为更聪明的做法？
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0,head)
        cur = head
        l,i = 0,0
        # while cur是cur指向到尾指针（None），while cur.next是将cur指向到链表的最后一个节点
        while cur:
            cur = cur.next
            l += 1
        cur = dummyNode
        # i<4(0123)
        while i < l-n:
            i += 1
            cur = cur.next
        cur.next = cur.next.next
        return dummyNode.next
s = Solution()
s.removeNthFromEnd(ListNode(1,None),1)
#方法二：栈
class Solution_1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0,head)
        cur = dummyNode
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        pre_node = stack[-1]
        pre_node.next = pre_node.next.next
        return dummyNode.next
s_1 = Solution_1()
s_1.removeNthFromEnd(ListNode(1,None),1)
#方法三：快慢指针（双指针）,由于我们需要找到倒数第 n 个节点，因此我们可以使用两个指针first 和 second 同时对链表进行遍历，并first 比second
# 超前 n 个节点。当first 遍历到链表的末尾时，second 就恰好处于倒数第n 个节点。
# 初始时，都指向head节点，然后让first先走n个节点，使first与second中间有n-1个节点，然后逐步遍历双指针，等first遍历到链表的末尾时，second正好在第倒数第n个节点
# 另外，由于删除链表节点知道其前驱节点会比较好删除，所以在head前面设置哑节点dummy node，这样first在链表末尾时，second指向的是倒数第n个节点的前驱节点。
class Solution_2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
s_2 = Solution_2()
s_2.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None))))),2)






