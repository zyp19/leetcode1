"""7.整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围[−231, 231 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 示例 1：
# 输入：x = 123
# 输出：321
# 示例 2：
# 输入：x = -123
# 输出：-321
# 示例 3：
# 输入：x = 120
# 输出：21
# 示例 4：
# 输入：x = 0
# 输出：0
"""
"""
思路：先把整数转化成string,这样做报错了，报错详情：
  File "/media/sda/zyp/project/leetcode/reverse.py", line 28, in reverse
    s[i+1] = s[len(s)-1-i]
TypeError: 'str' object does not support item assignment
错误原因是Python中的字符串不可改变，即无法直接修改字符串的某一位字符，或者是这种实例：
name = "Jone"
name[0] = "L"
print(name)#运行结果报错，提示TypeError: 'str' object does not support item assignment
https://www.cnblogs.com/Jonepeng/p/11152371.html
"""
# class Solution:
#     def reverse(self, x: int):
#         s = str(x)
#         # 2的6次方为64，且一位存放符号
#         if len(s) >=6:
#             return -1
#         result = s
#         for i in range(len(s)):
#             if len(s)-1-i >= 0:
#                 if s[len(s)-1]!=0:
#                     result[i+1] = s[len(s)-1-i]
#                 else:
#                     result[i+1] = s[len(s)-2-i]
#         result = int(s)
#         if result > 2**31-1 | result <-2**31:
#             return 0
#         return result
#
# solution = Solution()
# x = -123
# x = solution.reverse(x)
"""
正确解法
涉及到的知识：
1.python中的切片知识,python的切片生成了新的列表,返回的是一个新值：
1.1字符串的截取
①常规的：
s[1:3]
s[1:](当尾索引没有给出时，默认截取到字符串的末尾)
s[:3](当头索引没有给出时，默认从字符串的头部开始)
s[:](当尾索引和头索引都没有给出的时候，默认返回整个字符串，不过这只是一个浅拷贝)
②不常规的：
当头索引为负数时，则是指从字符串的尾部开始计数，最末尾的字符记为-1，以此类推，因此此时应该注意尾索引的值，
尾索引同样可以为负数，如果尾索引的值指明的字符串位置小于或等于头索引，此时返回的就是空字符串
注意，只是计数时候是从尾部计，但是截取后的字符串却不是从尾部开始出。
s = 'lang'
print(s[-2:])-->ng
print(s[-2:-2])-->''
print(s[-4:])-->lang
③字符串反转
print(s[::-1])
1.2一些常用的字符串API：
①使用len()方法获取字符串长度
len(lang)
②使用in操作符判断某个子字符是否在字符串中
if 'g' in s:（即返回true或false）
    print("左一平能进大厂")
③使用max()和min()方法获取字符串中编码最值对应的字符，即在python中字符串是可以比较的
④使用*操作符对字符串进行重复
s*2-->langlang
⑤将字符串的第一个字符大写
'python'.capitalize()
# Python
⑥使用split()方法将字符串按照指定的字符串分隔，返回数组
'hello world'.split(' ')
# ['hello', 'world']
⑦使用upper()、lower()方法对字符串中所有字符大写、小写
‘python’.upper()
# PYTHON
'PYTHON'.lower()
# python
⑧使用isupper()、islower()方法判断字符串中所有的字符是否都是大写、小写
'ABC'.isupper()
# True
'Abc'.islower()
# False
⑨使用istitle()方法判断字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
'Hello World'.istitle()
# True
'I am A Boy'.istitle()
# False
⑩使用swapcase()方法对字符串中所有的字符进行大小写互转，即小写变大写，大写变小写
'Abc'.swapcase()
# aBC
11.使用join()方法连接字符串数组
a = 'hello world'.split()
'-'.join(a)
# hello-world
12.使用find()方法判断一个字符串中是否含有某个子字符串，三个参数，第一个为必须，是指需要搜索的字符串，第二个和第三个参数则是指搜索的起始位置和终止位置，
搜索得到则返回索引值，得不到则返回-1
'hello world'.find('llo')
# 2
'hello world'.find('lloe')
# -1
13.使用endswith()和startswith()方法判断一个字符串是否是以某个字符串结尾、开头，参数和find()一致
'hello'.startswith('he')
# True
'hello'.endswith('lle')
# False
14.使用count()方法获取某个字符在字符串中出现的次数
lang = 'aaa111223'
lang.count('a')
# 3
15.使用index()方法获取某个字符在字符串中首次出现的位置的索引
lang.index('a')
# 0
lang.index('1')
# 3

2.字符串和整数的转换问题：
字符串转整数 i = int (s)
整数转字符串 s = str (i)
3.python中或和且的写法，就是or and。
4.python中字符串不可改变，是指其中的字符不可逐一改变，但是整个字符串可以被另一个字符串覆盖。
"""
class Solution:
    def reverse(self, x: int):
        s = str(x)
        # 2的6次方为64，且一位存放符号,这里也有问题，32位整数是真的32位
        if len(s) >=64:
            return -1
        if x == 0:
            return 0
        if x > 0:
            result = s[::-1]
            result = int(result)
        else:
            x = -x
            s = str(x)
            result = s[::-1]
            result = int(result)
            result = -result
        if result > 2**31-1 | result <-2**31:
            return 0
        else:
            return result

solution = Solution()
x1 = -123
x1 = solution.reverse(x1)
x2 = 0
x2 = solution.reverse(x2)
x3 = 467
x3 = solution.reverse(x3)
x4 = -120
x4 = solution.reverse(x4)
print(x1)
print(x2)
print(x3)
print(x4)




