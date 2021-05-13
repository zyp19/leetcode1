"""494.目标和
给你一个整数数组 nums 和一个整数 target。向数组中的每个整数前添加'+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
输入：nums = [1,1,1,1,1], target = 3输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""
"""
1.状态是 整数数组的值 和target
  选择是加或减值 得到目标整数
2.dp数组的定义是通过加或减数组的值等于target的方案个数
一开始我的dp数组定义写对了！但是不知道该怎么写状态转移方程啊！因为感觉好像没有子问题，方案与方案之间怎么能有子问题呢？
写的dp数组实际上不对哈！
"""
# from typing import List
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         for i in range(1,len(nums)+1):
#             for sum in range(1,target+1):
#                     dp[i][sum] = dp[i-1][sum-nums[i-1]]-nums[i-1]
"""
1.状态是 整数数组的值 和target
  选择是加或减值 得到目标整数
2.dp数组的定义是通过加或减数组的值得到的值
这样定义是不对的，因为第二个循环遍历target已经在算值了！
"""
# from typing import List
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         for i in range(1,len(nums)+1):
#             for sum in range(1,target+1):
#                 if sum > target:
#                     dp[i][sum] = dp[i-1][sum-nums[i-1]]-nums[i-1]
"""positive = sum（元素之和） - negative(前面是负号的元素)，dp数组为背包容量为positive，装入前i个重量为nums的物品的方案个数"""
"""其实不对，背包的容量含有变量negative，所以需要再转化下该公式：positive = sum - negative, sum-negative-negative = target,
negative = (sum-target)/2，dp数组为背包容量为negative，装入前i个重量为nums的物品的方案个数
1.状态：背包的容量(sum-target)/2 物品
2.dp数组的定义 将前i个重量为nums物品放入背包的方案个数；要求的值：dp[len(nums)][neg]；base case：dp[0][0]=1 dp[0][...]=0
3.通过选择寻找状态转移方程:不放进去 dp[i][w]=dp[i-1][w]  放进去 dp[i][w]=dp[i-1][w-nums[i]]+dp[i-1][w]
对于这两种状态转移方程的解释：不放进背包时，方案只有一种，就是等于前一个物品放入当前重量w的个数dp[i-1][w]；放入背包时，方案有两种，
前一个物品放入背包的的方案个数和当前背包的放入背包的方案个数的总和。
"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        negative = sum(nums)-target
        if negative < 0 or negative % 2!=0:
            return 0
        negative = int(negative/2)
        dp = [[0 for w in range(negative+1)]for i in range(len(nums)+1)]
        dp[0][0] = 1
        for w in range(negative+1):
            dp[0][w] = 0
        # 我觉得这道题要注意初始化的时候仅有dp[0][0]被初始化为0，当背包的重量为0的时候,因为数组里的数有可能是正的有可能是负的，所以需要使w从0开始
        for i in range(1,len(nums)+1):
            for w in range(negative+1):
                if w - nums[i-1] < 0:
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = dp[i-1][w]+dp[i-1][w-nums[i-1]]
        return dp[len(nums)][negative]




