"""438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：字母异位词指字母相同，但排列不同的字符串。 bac acb abc
"""
"""
思路：使用两个字典记录一下每个字符（作为键）出现的次数（值），使用的函数是：dict.get(key,0)用于初始化（当键不存在时）或者计数（当键存在时）
也可以使用dict.setdefault(key,0)，道理是一样的。
有了字典记录次数，那么就可以比较每个字符出现在窗口的次数，如果次数相等，则说明窗口中的字符是p的一个排列，如果说相等的话就要注意收缩窗口，因为这时候
已经到了下一个字符了，说明这个字符进不去窗口（因为有重复的），所以这时候就要收缩窗口。
"""
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        l ,r = 0 ,0
        res = []
        flag ,target ={},{}
        for c in p:
            # 是计算字典中每个键的值，如果键不存在的话，将该值置0，相当于为键做了一个初始化的操作。
            target[c] = target.setdefault(c,0)+1
        while r < len(s):
            if s[r] not in target:
                l = r+1
                flag.clear()
            else:
                flag[s[r]] = flag.setdefault(s[r],0)
                # 不符合题意时，收缩左指针。题意是窗口内是p的一个字母异位词，也就是如果存在字典flag中的某个字符的值和target相等了，那么下面flag[s[r]] += 1
                # 一定会使得flag中的值大于target中的，因此这种情况下要收缩左指针。
                while flag[s[r]] == target[s[r]] :
                    flag[s[l]] -= 1
                    l += 1
                # 计算结果
                if r - l + 1 == len(p):
                    res.append(l)
                flag[s[r]] += 1
            # 更新窗口
            r += 1
        return res
solution = Solution()
res = solution.findAnagrams("cbaebabacd","abc")
print(res)






