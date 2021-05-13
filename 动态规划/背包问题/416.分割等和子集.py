"""416.分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
"""
"""
本质上是一个背包问题，两个子集有元素和相等，即挑一些元素之和为sum/2的元素，即挑一些物品，使其重量之和等于sum/2。转化到问题中，dp数组前i个物品
的重量之和等于sum/2的方案是否存在，因此，dp数组是一个布尔值。且最后返回值应是dp[N][sum/2]的值。
1.明确状态，也就是dp数组的下标：背包的容量和可选择的物品
2.明确dp数组的定义：前i个物品在w重量是否可以放入背包中，即前i个数之和是否为j。明确最终要求的是dp数组的哪个状态：求dp[N][sum/2]。明确dp数组的base case：dp[0][...]=False dp[..][0]=True
3.根据选择明确状态转移方程：选择是把不把第i个物品装入背包中。如果第i个物品不装入背包，那么是否能够恰好装满背包，取决于上一个状态dp[i-1][j]，如果把第i个物品装入背包，那么是否能够恰好装满背包，
取决于dp[i-1][j-nums[i-1]]or dp[i-1][j]的状态

需要注意的细节问题：
"""
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        sums = int(sums/2)
        dp = [[False for w in range(sums+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1,len(nums)+1):
            for w in range(1,sums+1):
                # 第i个物品放不进w
                if w - nums[i-1] < 0:
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = dp[i-1][w] or dp[i-1][w-nums[i-1]]
        return dp[len(nums)][sums]


