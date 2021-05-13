"""
小明得到一个只包含大小写英文字母的字符串s，下标从1开始计算。现在他希望得到这个字符串下标的一个奇怪的集合。这个奇怪的集合需要满足的条件是：
1. 集合中的任意下标i对应的字母s[i]必须是小写字母 （islower()）
2. 对于集合中的任意两个下标i、j，对于任意数字k，i<=k<=j，有s[k]是小写字母（）
3. 集合中的下标对应的字母是两两不同的（去除重复）
4. 集合中的数字尽可能的多（废话）
帮助小明计算这个集合最多可以有多少下标(个)。
aaBBBabBaAb 2
"""
def function(s):
    out_list = set()
    for i in range(len(s)):
        if s[i].islower():
            out_list.add(s[i])
    return len(out_list)
result = function("aabbcc")
print(result)




