"""3. 无重复字符的最长子串（第一遍没有做出来）
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""
"""
思路：
1.去除重复字符（涉及到去重问题）
2.长度最长
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        result = []
        if s == "":
            return 0
        elif s == " ":
            return 1
        elif s!="":
            p = 0
            # 设立一个指针p，记录当前字串的头索引
            for i in range(1,len(s)):
                for j in range(p,i):
                    if s[j] != s[i]:
                        continue
                    elif s[j] == s[i] and p!=0:
                        result.append(s[p:i])
                        p = i
                    elif s[j] == s[i] and p == 0 and i!=len(s)-1:
                        p = i
                    elif s[j] == s[i]:
                        return 1
            if p != len(s)-1:
                result.append(s[p:])
            if p == 0:
                return len(s)
            a = 0
            if len(result) == 1:
                return len(result[0])
            for m in range(1, len(result)):
                if len(result[m])>len(result[m-1]):
                    a = len(result[m])
                else:
                    a = len(result[m-1])
            return a

solution = Solution()
a=solution.lengthOfLongestSubstring(s = "aa")
print(a)







