"""1. 两数之和
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 targe的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


# 链表遍历、链表相加（引入sum值进行加和）、考虑链表长度不一样、考虑进位
class listNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def twoSum(listNode1, listNode2):
    for node in range(listNode1.val):
        if(node.next != None):
            print(node.val)
    for node in range(listNode2.val):
        if(node.next != None):
            print(node.val)

if __name__ == '__main__':
    listNode1 = listNode([2, 4, 3])
    listNode2 = listNode([5, 6, 4])
    twoSum(listNode1,listNode2)



