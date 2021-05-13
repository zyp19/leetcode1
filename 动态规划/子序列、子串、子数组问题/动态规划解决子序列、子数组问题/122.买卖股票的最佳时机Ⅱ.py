"""122.买卖股票的最佳时机Ⅱ
给定一个数组 prices ，其中prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
"""
"""
方法一：
算法可以直接简化为只要今天比昨天大，就卖出。
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit
"""
方法二：动态规划
1.考虑状态和dp数组的定义：
考虑到不能参与多笔交易，因此每次交易完毕的状态是手里有一支股票或没有股票的状态。所以分为两种状态：dp[i][0]是第i天交易完毕手里没有股票的最大利润，dp[i][1]是第i天交易完毕手里有股票的最大利润。
2.考虑状态转移方程：
dp[i][0]=max(dp[i-1][0],dp[i-1][1]+price[i])，意为当前手里没股票的原因是与前一天的状态有关的，因为不能参与多笔交易，所以如果前一天手里
有股票dp[i-1][1]，就要卖掉它+price[i]，如果前一天没有股票dp[i-1][0]，就直接转移到今天的状态，还要比较一下这两种谁的利润大，所以是max。
dp[i][1] = max(dp[i-1][1],dp[i-1][0]-price[i])，意为当前手里有股票的原因是与前一天的状态是有关的，如果前一天手里有股票dp[i-1][1]就直接转移过来，
如果前一天手里没有票dp[i-1][0]，那么为了今天有，就要在今天买入，所以利润就会减少price[i]。
3.考虑base case的情况：
dp[0][0]没有=0，dp[0][1]有=-price[0]
持有股票的收益一定低于不持有股票的收益，因此这时候ddp[n−1][0] 的收益必然是大于dp[n−1][1]的，最后的答案即为dp[n−1][0]。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 注意细节
        dp = [[0 for i in range(2)] for i in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[len(prices)-1][0]
"""
方法三：贪心算法：贪心的角度考虑我们每次选择贡献大于 0的区间即能使得答案最大化，因此最后答案为 ans = max(0, prices[i] - prices[i - 1])
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit
