"""14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
（第一遍没有做出来的原因是对字符串的切片操作不够熟悉）
"""
class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            return []
        if len(strs) == 1:
            return strs
        else:
            i = min(strs)
            j = max(strs)
            for n,s in enumerate(i):
                if s == j[n]:
                    if n == len(i):
                        return i
                    else:
                        continue
                else:
                    return s[0:n]

solution = Solution()
solution.longestCommonPrefix(["flower","flow","flight"])

