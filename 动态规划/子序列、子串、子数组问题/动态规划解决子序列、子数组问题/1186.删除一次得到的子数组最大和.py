"""1186.删除一次得到子数组最大和
给你一个整数数组，返回它的某个非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。
换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组
（剩下）的元素总和是所有子数组之中最大的。
注意，删除一个元素后，子数组 不能为空。
"""
"""
dp数组的含义是以nums[i]为结尾的最大元素总和，dp[i]=max(nums[i],dp[i-1],dp[i-1]+nums[i],sum(arr))
"""
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [0 for i in range(len(arr))]
        dp[0] = arr[0]
        res = 0
        for i in range(1,len(arr)):
            for j in range(i):
                del_one = sum(arr[0:j] + arr[j + 1:i])
                # 问题在于不能把dp[i-1]和dp[i-1]+arr[i]放在一起，因为定义不同，dp[i-1]代表删除当前以下标i的元素，
                # 如果连续好几个负值元素出现，像[1,-2,-2,3]，就会发生连续好几次不取-2，这与连续子数组是相悖的，所以必须把有删除元素的和不删除元素的分开定义
                dp[i] = max(del_one,arr[i],dp[i-1],dp[i-1]+arr[i])
        for i in range(len(dp)):
            res = max(res,dp[i])
        return res
s = Solution()
s.maximumSum([1,-2,-2,3])
#   正确答案：
# dp[i][0]表示以nums[i]为结尾的最大元素和
# dp[i][1]表示以nums[i]为结尾的删除任意元素的最大元素和，dp[i-1][1]+arr[i]表示删除[0,i-1]中的某个元素，不删下标i的元素；dp[i-1][0]表示删除第i个元素
class Solution_1:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        ans = -float('inf')
        dp = [[-float('inf')] * 2 for _ in range(n)]
        for i in range(n):
            dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i-1][1] + arr[i], dp[i-1][0])
            ans = max(ans, dp[i][0], dp[i][1])
        return ans


