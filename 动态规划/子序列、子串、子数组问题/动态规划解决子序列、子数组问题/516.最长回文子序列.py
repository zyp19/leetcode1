"""516.最长回文子序列
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for j in range(len(s)+1)] for i in range(len(s)+1)]
        for i in range(len(s)):
                dp[i][i] = 1
        for i in range(len(s)-2,0,-1):
            for j in range(i+1,len(s)+1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[1][len(s)]