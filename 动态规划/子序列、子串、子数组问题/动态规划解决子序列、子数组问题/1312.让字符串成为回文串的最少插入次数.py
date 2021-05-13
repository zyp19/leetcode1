"""1312.让字符串成为回文串的最少插入次数
给你一个字符串s，每一次操作你都可以在字符串的任意位置插入任意字符。
请你返回让s成为回文串的最少操作次数。
「回文串」是正读和反读都相同的字符串。
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j-1])+1
        return dp[0][len(s)-1]
