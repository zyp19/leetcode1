"""438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
字母异位词指字母相同，但排列不同的字符串。 bac acb abc
不考虑答案输出的顺序。
"""
"""
思路：（知识点1）滑动窗口模板：
最外层循环为右指针循环while right < len(s):
 更新窗口信息
 while循环，循环条件是窗口信息是否符合题中条件来控制左指针的移动
 这里的循环条件是验证一下s中的字母异位词在p的窗口中的个数，如果相等，则说明s中的窗口中的字母是p中的一个排列，如果不相等，此时应右移一次左指针
滑动窗口重要的不是模板，而是细节，根据题目中的一些细节才能做出来
（知识点2）字典/集合记录每个字符在字符串中出现的个数，对于该题来说，先用字典记录了每个字符出现在p中次数，然后再用另一个字典记录一下在s的窗口中出现的次数，这样的好处是。
每个字符只能在字典中存放唯一一次键，而值（出现次数）可以有多次，从而可以计算一下出现的次数，如果不相等的话，就要收缩窗口。
"""
"""
不理解之处，细节，很重要的地方：
和标准代码相比，有3个问题不能理解（或者说人家巧妙之处、或者说我想不到的地方）：
1）设置nums，记录窗口中的字符的个数，十分巧妙，需要再思考一下
2）当当前字符在字典中的个数和target中的该字符的个数相等时，即temp == target[right]的时候呢，为什么要是flag[s[left]] -= 1，而不是
flag[s[right]] -= 1
3)为什么要提前记录一下flag[s[right]]的值，不理解！（其实是不用的）
"""
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) == 0:
            return 0
        res = []
        flag, target = {}, {}
        left, right ,nums = 0, 0 ,0
        for c in p:
            target[c] = target.get(c,0) + 1
        while right < len(s):
            if s[right] not in target:
                left ,right = right + 1,right + 1
                flag.clear()
            else:
                # 当相等的时候，右指针是不可能右移的，一定是在缩小窗口。因此这个关于条件满足的循环，其中的东西一定是管着左指针的！
                flag[s[right]] = flag.get(s[right], 0)
                while flag[s[right]] == target[s[right]] :
                    flag[s[left]] -= 1
                    left += 1
                    nums -= 1
                #     当条件满足的时候，就更新（增大）窗口
                flag[s[right]] += 1
                right += 1
                nums += 1
                if nums == 1:
                    res.append(left)
        return res
solution = Solution()
res = solution.findAnagrams("cbaebabacd","abc")
print(res)







