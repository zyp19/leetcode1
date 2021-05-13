class Solution:
    def hasCycle(self, head):
        slow = head
        if slow ==None or slow.next == None:
            return False
        fast = head.next
        while slow != fast :
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True