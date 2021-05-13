# 二题：货运装箱问题
# 题目描述：
# 货轮最大重量C，有N个集装箱，每个集装箱重量W(i)，对应货物价值V(i)。求货轮不超过最大载重的前提下装载货物总价值最大。
# 输入：第一行最大重量C，第二行每个集装箱重量W(i)，第三行每个集装箱价值V(i)。
# 输出：货物总价值。
def knapsack(W,N,wt,val):
    dp = [[0]*(N+1)]*(W+1)
    for i in range(1,N):
        for w in range(1,W):
            if w - wt[i-1] <0:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w-wt[i-1]] + val[i-1],dp[i-1][w])
    return dp[N][W]
r = knapsack(4,3,[2,1,3],[4,2,3])
print(r)
