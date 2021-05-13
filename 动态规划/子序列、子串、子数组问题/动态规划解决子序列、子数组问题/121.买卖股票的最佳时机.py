"""121.买卖股票的最佳时机
给定一个数组 prices ，它的第i个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
"""
"""
6.28思路：和最大有点像，数组的值一定是正的，求连续子数组的
以nums[i]为结尾的最大子序列差（利润），但是从dp[i-1]退不出dp[i]，因为利润与利润之间没有关系
求nums[i]为结尾的最长递增子序列，也不对，不一定能保证元素差最大。
放弃动态规划，想不出dp
方法1：
用滑动窗口做，当利润小于0时，就左移窗口。
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,res = 0,0,0
        while r < len(prices):
            c = prices[r]
            r += 1
            res = max(res,c-prices[l])
            while c - prices[l] < 0:
                l += 1
        return res
"""
方法2：遍历数组，记录最小价格和最大利润
"""
def maxProfit_1(prices):
    minPrice = float("-inf")
    maxValue = 0
    for price in prices:
        minprice = min(minPrice,price)
        maxValue = max(maxValue,price-minprice)
    return maxValue
"""
股票问题的方法就是 动态规划，因为它包含了重叠子问题，即买卖股票的最佳时机是由之前买或不买的状态决定的，而之前买或不买又由更早的状态决定的
方法3：动态规划法：dp的定义是前i天的最大利润，因此dp = max(dp[i-1],price[i]-minprice)
"""
def maxProfit_2(prices):
    dp = [0 for i in range(len(prices))]
    minPrice = prices[0]
    for i in range(1,len(prices)):
        minPrice = min(minPrice,prices[i])
        dp[i] = max(dp[i-1],prices[i] - minPrice)
    return dp[len(prices)-1]