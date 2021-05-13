"""考察指数：*****
注意和数组归并排序的不同之处
可以用小根堆优化

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        # 链表放在二维数组中，可把它转化为一维的思想
        size = len(lists)
        if size == 0 or lists is None:
            return None
        return self.merge_sort(lists,0,size-1)

    def merge_sort(self,lists,low,high):
        # 这一步真的特别重要，当只有一个元素时，此时应该初始化一下第一个元素中的值，不然就得不到返回的链表元素。而数组的归并排序不需要，因为不需要返回值，直接走了merge()即可
        if low == high:  # 只有一个
            return lists[low]
        if low < high:
            mid = (low+high)//2
            leftNode = self.merge_sort(lists,low,mid)
            rightNode = self.merge_sort(lists,mid+1,high)
            return self.merge(leftNode,rightNode)

    def merge(self,l1,l2):
        newNode = ListNode()
        h = newNode
        while l1 and l2:
            if l1.val < l2.val:
                h.next = ListNode(l1.val)
                l1 = l1.next
            else:
                h.next = ListNode(l2.val)
                l2 = l2.next
            h = h.next
        if l1:
            h.next = l1
        else:
            h.next = l2
        return newNode.next