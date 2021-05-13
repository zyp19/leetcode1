"""697.数组的度
给定一个非空且只包含非负数的整数数组nums，数组的度的定义是指数组里任一元素出现频数的最大值。你的任务是在 nums 中找到与nums拥有相同大小的度的最短连续子数组，返回其长度。
输入：[1, 2, 2, 3, 1]输出：2
解释：输入数组的度是2，因为元素1和2的出现频数最大，均为2.连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2] 最短连续子数组[2, 2]的长度为2，所以返回2.
"""
from typing import List
from collections import Counter
class Solution_1:
    def findShortestSubArray(self, nums: List[int]) -> int:
        need,window = Counter(),Counter()
        length = float("inf")
        for c in nums:
            need[c] += 1
        # nums数组的度
        d = max(need.values())
        # 滑动窗口法
        l,r,valid = 0,0,0
        while r < len(nums):
            c = nums[r]
            r += 1
            window[c] += 1
            if window[c] == d:
                valid = d
            # print(l,r,d,valid)
            while valid == d:
                # 更新窗口
                if r - l < length:
                    length = r - l
                a = nums[l]
                l += 1
                # 窗口收缩的条件不对：如果window[a]等于d的情况下就不会收缩窗口，且如果后面有一个更小的length，就会出错，应该记录当前的c值，也就是进入while循环更新窗口的r值
                if window[c]==d:
                    valid -= 1
        return length
# s = Solution()
# print(s.findShortestSubArray([2,1,1,2,1,3,3,3,1,3,1,3,2]))

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        need,window = Counter(),Counter()
        length = float("inf")
        for c in nums:
            need[c] += 1
        # nums数组的度
        d = max(need.values())
        l,r = 0,0
        while r < len(nums):
            c = nums[r]
            r += 1
            window[c] += 1
            while window[c] == d:
                # 更新窗口
                if r - l < length:
                    length = r - l
                a = nums[l]
                window[a]-=1
                l += 1
        return length
s = Solution()
print(s.findShortestSubArray([2,1,1,2,1,3,3,3,1,3,1,3,2]))

# 动态规划法：


