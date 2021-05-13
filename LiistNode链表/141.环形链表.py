"""141. 环形链表
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置
（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
"""
"""
1.快慢指针问题介绍（龟兔赛跑问题）
该题使用的是一步两步快慢指针：
假想「乌龟」和「兔子」在链表上移动，「兔子」跑得快，「乌龟」跑得慢。当「乌龟」和「兔子」从链表上的同一个节点开始移动时，如果该链表中没有环，那么「兔子」将一直处于
「乌龟」的前方；如果该链表中有环，那么「兔子」会先于「乌龟」进入环，并且一直在环内移动。等到「乌龟」进入环时，由于「兔子」的速度快，它一定会在某个时刻与乌龟相遇，
即套了「乌龟」若干圈。
思路：即设置两个指针,一快一慢，slow指向head,fast指向head.next，且每次slow移动一个节点，fast移动两个结点，在移动之前要判断一下fast及fast.next是否
为None，如果是的，说明这个链表不是有环的，直接就返回false即可。
另外要注意一下边界情况，空链表要排除。
2.其他方法
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 这种思路的时间复杂度是O(N),空间复杂度：O(1)O(1)。我们只使用了两个指针的额外空间。
class Solution:
    def hasCycle(self, head: ListNode):
        slow = head
        # 边界值的判断同样也需要注意，因为边界值slow =None说明链表是不存在的；slow.next为None，说明fast指针会指向None，也是说明链表是无环的。
        if slow ==None or slow.next == None:
            return False
        fast = head.next
        while slow != fast :
            # 为什么fast要设置两个None，原因是，fast是两步走的，如果刚好走到fast为None是可能的，或者刚好走到fast不为None但是fast.next为None，这样slow
            # 可能会不为None，但是slow.next为None，这种情况下执行while循环条件满足就会无限循环了。
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True