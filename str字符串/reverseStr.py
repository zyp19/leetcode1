"""编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""
'''
1.python中的字符串""和字符''没有太大的区别，只区别于转义字符和引号中含引号的情况
2.时间复杂度和空间复杂度的知识：https://leetcode-cn.com/problems/reverse-string/comments/
3.注意，s[::-1] 和return s[::-1]都是不行的，因为s[::-1]是返回一个新值，并不是对s就地修改。 s = s[::-1] 是返回一个新值赋给新的变量s。
如果要做到就地修改，那么是要 切片 = 切片 如下所示
class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]
'''
# import math
# class Solution:
#     def reverseString(self, s):
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         j = math.floor(len(s)-1)
#         for i in range(int(j / 2)):
#             temp1 = s[len(s)-1-i]
#             temp2 = s[i]
#             s[i] = temp1
#             s[len(s)-1-i] = temp2
#         print(s)
# solution = Solution()
# solution.reverseString(["h","e","l","l","o"])
"""
python的数据交换比较方便，比如交换a,b的值可以这样：
a,b = b,a
如果是使用c/c++语言的话，需要一个临时变量，保存一个值，这样：
tmp = a;
a = b;
b = tmp;
"""
class Solution:
    def reverseString(self, s) :
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)
solution = Solution()
solution.reverseString(["h","e","l","l","o"])