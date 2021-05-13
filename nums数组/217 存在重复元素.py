"""217 存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
"""
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]):
        new_set = set()
        for num in nums:
            new_set.add(num)
        if len(new_set) == len(nums):
            return False
        else:
            return True
solution = Solution()
flag = solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(flag)
