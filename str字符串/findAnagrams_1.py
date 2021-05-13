"""
该方法不好用！虽然是模板，但不符合逻辑，不好用！！！！
"""
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        need, window = {}, {}
        for c in p:
            if c in need.keys():
                need[c] += 1
            else: need[c] = 1
        l, r,valid = 0, 0, 0
        res = []
        while r < len(s):
            cur = s[r]#右入
            r += 1
            if cur in need.keys():#窗口内操作,右指针
                if cur in window.keys():
                    window[cur] += 1
                else:
                    window[cur] = 1
                if window[cur] == need[cur]:
                    valid += 1
            while r-l >= len(p):
            	# 根据题意选择输出结果
                if valid == len(need):
                    res.append(l)
                cur = s[l]#左出
                l += 1
                if cur in need.keys():#窗口内操作
                    if window[cur] == need[cur]:
                        valid -= 1
                    window[cur] -= 1
        return res