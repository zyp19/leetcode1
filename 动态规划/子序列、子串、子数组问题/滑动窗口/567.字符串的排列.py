"""567.字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
"""
"""
思路：window和need是完全相等的,注意，是一个排列就可以
"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str):
        valid = 0
        l,r = 0,0
        need,window = Counter(),Counter()
        for c in s1:
            need[c] += 1
        while r < len(s2):
            c = s2[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while r - l >= len(s1):
                if valid == len(need):
                    return True
                d = s2[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
            return False
