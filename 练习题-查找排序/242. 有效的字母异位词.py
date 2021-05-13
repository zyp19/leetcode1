"""给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词(即重新排列后组成的单词)。
示例1:
输入: s = "anagram", t = "nagaram"
输出: true
示例2:
输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
"""
class Solution:
    def isAnagram(self, s: str, t: str):
        # 字典的初始化
        dict1 = {}
        dict2 = {}
        for i in s:
            # 1.注意dict[i]+=1是错误的
            # 字典存在一开始没有值的情况，所以不能直接就赋值
            dict1[i] = dict1.get(i,0) + 1
        for m in t:
            dict2[m] = dict2.get(m,0) + 1
        #     下面的部分都是比较两个字典的，是先比较的key是否相同，再比较value是否相同
        # 可以用一句话了结两个字典的比较：return dict1 == dict2 Python内部对==进行了重载，帮你实现了对key和value进行判断。
        if len(dict1) != len(dict2):
            return False
        elif dict1.keys() != dict2.keys():
            return False
        else:
            for i in s:
                if dict1[i] == dict2[i]:
                    continue
                else:
                    return False
            return True
so = Solution()
re = so.isAnagram(s = "rat", t = "car")
print(re)



