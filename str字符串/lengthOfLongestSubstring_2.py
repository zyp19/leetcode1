"""3. 无重复字符的最长子串（集合法已经用过了，这次再试试字典法？）
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
"""
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self,s):
        if len(s) <= 1:
            return len(s)
        left, right, nums = 0,0,0
        flag = {}
        while right < len(s):
            # 或者是flag[s[right]] = flag.get(s[right],0)+1，那下面的flag[s[right]] += 1就去掉，原因是这句话不影响后面的值所以放下面或放上面都行
            # 如果是影响下面的值判断的话，就得在下面写
            flag[s[right]] = flag.get(s[right],0)
            # 当不符合题意的时候，即右指针遇到了重复字符，或者说右指针指向的字符在字典中的值大于1，就收缩左窗口。
            while flag[s[right]] == 1:
                # 窗口缩小时，要更新什么样的数据？一定会更新的是左指针的值
                flag[s[left]] -= 1
                left += 1
            # 计算结果
            if (right - left + 1) > nums :
                nums = right - left + 1
            # 更新窗口的意思就是右移右指针
            flag[s[right]] += 1
            right += 1
        return nums
solution = Solution()
nums = solution.lengthOfLongestSubstring("abcabcbb")
print(nums)


