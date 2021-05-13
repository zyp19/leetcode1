"""3. 无重复字符的最长子串（第一遍没有做出来）
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        a = set()
        i , j, result= 0 , 0, 0
        while i < len(s):
            # 含有重复字符,收缩左窗口
            while s[i] in a:
                a.remove(s[j])
                j += 1
            # 不含有重复字符
            a.add(s[i])
            result = max(result, i - j + 1)
            i += 1
        return result
solution = Solution()
result = solution.lengthOfLongestSubstring("dvdf")
print(result)