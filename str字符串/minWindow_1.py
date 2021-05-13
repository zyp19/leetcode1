"""76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
输入：s = "ADOBEC ODE BANC", t = "ABC"
输出："BANC"
输入：s = "a", t = "a"
输出："a"
分几种情况：
1.
"""
class Solution:
    def minWindow(self,s,t):
        flag,target = {},{}
        for i in t:
            target[i] = target.get(i,0) + 1
        for i in s:
            flag[i] = flag.get(i,0)
        l,r,length= 0,0,0
        result = ""
        while l < len(s):
            # 保证s的第一个字符是在t中的
            if s[l] in target:
                r = l
                # 条件是“s涵盖t所有字符的最小子串”
                if s[r] in target:
                    if flag[s[r]] != target[s[r]] and len(flag) != len(target):
                        flag[s[r]] = flag.get(s[r],0)+1
                        r += 1
                    else:
                        r += 1
                else:

                # 获取一个值
                if r-l+1 < length:
                    length = r-l+1
                    result = str[l:r]
                flag = {}
                l = r+1
            else:
                l += 1
        return result
solution = Solution()
length = solution.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(length)




