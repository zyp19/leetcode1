"""1807. 替换字符串中的括号内容
给你一个字符串s，它包含一些括号对，每个括号中包含一个 非空的键。
比方说，字符串"(name)is(age)yearsold"中，有两个括号对，分别包含键"name" 和"age"。
你知道许多键对应的值，这些关系由二维字符串数组knowledge表示，其中knowledge[i] = [key i, value i]，表示键key i对应的值为value i。
你需要替换 所有的括号对。当你替换一个括号对，且它包含的键为keyi时，你需要：
将key i和括号用对应的值valuei替换。
如果从 knowledge中无法得知某个键对应的值，你需要将key i和括号用问号"?"替换（不需要引号）。
knowledge中每个键最多只会出现一次。s中不会有嵌套的括号。
请你返回替换 所有括号对后的结果字符串。
"""
"""
思路：本题涉及到的知识点有：
1.二维数组转化为字典格式
2.栈的运用
3.字符串的拼接
"""
from typing import List
class Solution:
    def evaluate(self, s: str, knowledge:List[List[str]]):
        # flag1 = []
        # i = 1
        # while i < len(s):
        #     if s[i-1] == '(':
        #         while s[i] != ')':
        #             flag1.append(s[i])
        #             i += 1
        #     elif s[i-1] != '(':
        #         i += 1
        #         continue
        # return flag1

        stack = []
        result = ""
        dict = {}
        flag = False
        for item in knowledge:
            dict[item[0]] = item[1]
        for i in s:
            if i == '(':
                flag = True
            elif i ==')':
                if flag:
                    result += dict.get(''.join(stack),'?')
                    stack=[]
                    flag = False
            else:
                if flag:
                    stack.append(i)
                else:
                    result += i
        return result

solution = Solution()
result = solution.evaluate("(name)is(age)yearsold",[["name","bob"],["age","two"]])
print(result)


