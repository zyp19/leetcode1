"""152.乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
"""
# 思路：看到最大子数组之乘积，和最大子数组和道理一样，定义以nums[i]为结尾的最大连续子数组之际为dp[i]，dp[i] = max(dp[i-1]*nums[i],nums[i])即自成一派或与前面合二为一。
# [2,-5,-2,-4,3]
# 输出：
# 20
# 预期结果：
# 24
# 上面这个用例没有过
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        sum =nums[0]
        res = float("-inf")
        for i in range(1,len(nums)):
            sum = sum*nums[i]
            dp[i] = max(sum,dp[i-1]*nums[i])
        for i in range(len(dp)):
            res = max(res,dp[i])
        return res
# 错误原因：当前位置的最优解未必是由前一个位置的最优解转移得到的。
# 正确做法：如果当前位置是一个负数的话，希望以它的前一个位置结尾的某个段的积也是一个负数，这样就可以负负得正，并且希望这个积尽可能“负的更多”，即尽可能小。
# 如果当前位置是一个整数的话，更希望它以它前一个位置结尾的某个段的积也是一个整数，并且希望它能尽可能地大。
# 于是这里可以维护一个fmin(i)，表示以第i个元素结尾的乘积最小子数组的乘积！
class Solution_true:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0 for i in range(len(nums))]
        dp_min = [0 for i in range(len(nums))]
        dp_max[0] = nums[0]
        dp_max[0] = nums[0]
        res = float("-inf")
        for i in range(1,len(nums)):
            dp_max[i] = max(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        for i in range(len(nums)):
            res = max(res,dp_max[i])
        return res