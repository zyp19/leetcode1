"""3.无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

"""
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self,s):
        l,r,res = 0,0,0
        need, window = Counter(),Counter()
        for c in s:
            need[c] += 1
        while r < len(s):
            c = s[r]
            r += 1
            window[c] += 1
            while window[c] > 1:
                d = s[l]
                l += 1
                window[d] -= 1
            res = max(res,r - l)
        return res


