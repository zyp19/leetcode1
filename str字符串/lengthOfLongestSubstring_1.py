"""3. 无重复字符的最长子串（第一遍没有做出来）
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
"""
思路：去除重复字符——集合中不允许有重复字符，因此可以建一个集合，把所有子串放到一个集合中，然后求长度最长的。
leetcode有些题解说这种方法是使用了哈希表+双指针，其实哈希表的部分在本题中就是定义了一个集合来存储，也可以使用字典来存储。
"""
class Solution:
    def lengthOfLongestSubstring(self,s):
        if len(s) <= 1:
            return len(s)
        i = 0
        j = 0
        a = set()
        result = 0
        while j < len(s):
            while i < j and s[j] in a:
                a.remove(s[i])
                i += 1
            a.add(s[j])
            j += 1
            result = max(j - i , result)
        return result
solution = Solution()
i = solution.lengthOfLongestSubstring("dvdf")
print(i)