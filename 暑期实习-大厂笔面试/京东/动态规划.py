n=3
dp = []
dp[0] = 0
dp[1] = 1
dp[2] = 1
for i in range(2,n):
    dp[i] = dp[i-1] + dp[i-3]
print(dp[n])