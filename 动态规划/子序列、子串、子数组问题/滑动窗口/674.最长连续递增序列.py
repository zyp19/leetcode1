"""674.最长连续递增序列
给定一个未经排序的整数数组，找到最长且连续递增的子序列，并返回该序列的长度。
连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l],
nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
"""
"""
思路：使用滑动窗口双指针来做
"""
from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(set(nums)) == 1:
            return 1
        i,j,l = 0,1,0
        while j < len(nums):
            if nums[j] > nums[j-1]:
                j += 1
            else:
                i,j = j,j + 1
            l = max(l, j - i)
        return l
s = Solution()
print(s.findLengthOfLCIS([1,3,4,7,8,9,10,11]))
# print(s.findLengthOfLCIS([8,7,6,5,4,3,2,1]))