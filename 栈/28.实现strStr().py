"""28. 实现 strStr()
实现strStr()函数。给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回 -1 。
输入：haystack = "hello", needle = "ll"
输出：2
输入：haystack = "aaaaa", needle = "bba"
输出：-1
输入：haystack = "", needle = ""
输出：0
"""
"""
思路：我原本的思路是遍历这个hay这个字符串和needle进行比较，这样比较也可以
"""
class Solution:
    def strStr(self, haystack: str, needle: str):
        if len(needle)==0:
            return 0
        elif len(haystack)==0:
            return -1
        else:
            i,j,m=0,0,0
            while i < len(haystack):
                if haystack[i] == needle[0]:
                    j = i
                    m = 0
                    while j < len(haystack) and m < len(needle):
                        if haystack[j] == needle[m]:
                            j += 1
                            m += 1
                        else:
                            i=j
                            break
                    if len(haystack) == len(needle):
                        if j == len(haystack):
                            return 0
                    else:
                        if j == len(haystack):
                            return -1
                        elif m == len(needle):
                            return j - m
                else:
                    i += 1
            return -1

solution = Solution()
result = solution.strStr(haystack = "helollo", needle = "ll")
print(result)