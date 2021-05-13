"""经典的0-1背包问题：有N个物品，物品具有重量wt和价值val两个属性，背包具有容量W，现在让你用这个背包装物品，算一下背包能装下的最大价值是多少？"""
from typing import List
class Solution:
    def kanpsck(self,W:int,N:int,wt:List,val:List):
        # dp = [[0]*(N+1)]*(W+1)
        dp = [[0 for w in range(W+1)] for i in range(N+1)]
        for i in range(1,N+1):
            for w in range(1,W+1):
                if w-wt[i-1]<0:
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = max(dp[i-1][w],dp[i-1][w-wt[i-1]]+val[i-1])
        return dp[N][W]
s = Solution()
print(s.kanpsck(4,3,[2,1,3],[4,2,3]))
