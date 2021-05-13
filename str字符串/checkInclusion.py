"""567. 字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串 。
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str):
        flag, target={},{}
        l,r = 0,0
        for c in s1:
            target[c] = target.get(c,0)+1
        while r < len(s2):
            if s2[r] not in target:
                l = r + 1
                flag.clear()
            else:
                flag[s2[r]] = flag.get(s2[r],0)
                while flag[s2[r]] == target[s2[r]]:
                    flag[s2[l]] -= 1
                    l += 1
                if (r-l+1) == len(s1):
                    return True
                flag[s2[r]] += 1
            r += 1
        if r == len(s2):
            return False
solution = Solution()
result = solution.checkInclusion(s1 = "ab",s2 = "eidbaooo")
print(result)

