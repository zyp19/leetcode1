"""76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
"""
"""
输入：s = "ADOBECODE BANC", t = "ABC"
输出："BANC"
输入：s = "a", t = "a"
输出："a"
"""
class Solution:
    def minWindow(self, s: str, t: str):
        flag, target ={},{}
        l,r,nums=0,0,0
        res = []
        for c in t:
            target[c] = target.get(c,0)+1
        while r < len(s):
            if flag [s[r]]:

            else:
                if s[r] not in target:
                    l = r+1
                    flag.clear()
                else:
                    flag [s[r]] = flag.get(s[r],0)
                    while flag[s[r]] == target[s[r]]:
                        flag[s[l]] -= 1
                        l -= 1
                        nums -= 1
                    flag[s[r]] += 1
                    nums += 1
                    if nums==1:
                        res.append(s[l:r])
            r += 1

