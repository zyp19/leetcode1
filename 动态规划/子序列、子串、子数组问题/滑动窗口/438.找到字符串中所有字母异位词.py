"""438. 找到字符串中所有字母异位词
给定一个字符串s和一个非空字符串p，找到s中所有是p的字母异位词的子串，返回这些子串的起始索引。字符串只包含小写英文字母，并且字符串s和 p的长度都不超过 20100。
说明：字母异位词指字母相同，但排列不同的字符串。不考虑答案输出的顺序。
输入:s: "cbaebabacd" p: "abc"
输出:[0, 6]
解释:起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
"""
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        l,r = 0,0
        valid = 0
        need,window = Counter(),Counter()
        for c in p:
            need[c] += 1
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] += 1
                # c这个字符在足够了
                if need[c] == window[c]:
                    valid += 1
            print(l,r)
            while valid == len(need):
                if  r - l == len(p):
                    res.append(l)
                d = s[l]
                l += 1
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        return res
sa = Solution()
print(sa.findAnagrams("cbaebabacd","abc"))
