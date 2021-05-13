"""76.最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need = collections.defaultdict(int)  # 记录t中字符出现次数
        # window = collections.defaultdict(int)
        need,window = Counter(),Counter()
        valid,start = 0,0
        length = float("inf")
        for c in t:
            need[c] += 1
        l,r = 0,0
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            #  已经覆盖了t中的子串，因为vaild计数的是包含t中的子串的字符，注意算的是键值！
            while valid == len(need):
                # 我只能说一句牛逼！更新结果牛逼
                if r - l < length:
                    start = l
                    length = r - l
                d = s[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return s[start:start+length] if length != float("inf") else ""
s = Solution()
s.minWindow("ADOBEC ODEBANC","ABC")