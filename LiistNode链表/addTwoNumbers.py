class ListNode:
    def __init__(self, val, next = None):
            # 别拖了 快写
        self.val = val
        self.next = next
class Solution:
    #######单链表头指针的知识###############

    # 实际上，链表头指针就代表链表中的第一个结点；有时候在单链表的第一个结点之前附设一个结点，称为头结点；
    # 另外，单链表中可以没有头结点，但是 不能没有头指针，如果没有头结点则头指针直接指向第一个结点。
    def addTwoNumbers(self, head1, head2):
        head = ListNode(head1.val + head2.val)
        yesmola = head
        while(head1.next != None or head2.next != None):
            # 这两句写的也不够严谨，要延申下一个指针，应该判断一下这个结点是不是存在？如果不存在的话要定义一个结点才行
            head1 = head1.next if head1.next else ListNode()
            head2 = head2.next if head2.next else ListNode()
            yesmola.next = ListNode(head1.val + head2.val + yesmola.val // 10)
            yesmola.val = yesmola.val % 10
            yesmola = yesmola.next
        if(yesmola.val >= 10):
            # 这一句话就充分展示了对链表的理解不足，next是指针，应该是指向结点而不是结点中的值
            # yesmola.next = yesmola % 10
            yesmola.next = ListNode(yesmola.val // 10)
            yesmola.val = yesmola.val % 10
        return yesmola

solution = Solution()
head1 = ListNode([8,1,3])
head2 = ListNode([9,1,2])
solution.addTwoNumbers(head1, head2)




