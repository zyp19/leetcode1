"""53.最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""
from typing import List
# 连续子数组问题，设置dp数组的定义为以nums[i]结尾的最大子数组之和，因此为dp[i] = max(nums[i],dp[i]+nums[i])
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        res = float("-inf")
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],dp[i-1] + nums[i])
        for i in range(len(dp)):
            res = max(res,dp[i])
        return res



