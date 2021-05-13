"""1249. 移除无效的括号
给你一个由 '('、')' 和小写字母组成的字符串 s。
你需要从字符串中删除最少数目的 '(' 或者 ')'可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
请返回任意一个合法字符串。
有效「括号字符串」应当符合以下任意一条要求：
空字符串或只包含小写字母的字符串
可以被写作AB（A连接B）的字符串，其中A和B都是有效「括号字符串」
可以被写作(A)的字符串，其中A一个有效的「括号字符串」
示例 1：
输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
示例 2：
输入：s = "a)b(c)d"
输出："ab(c)d"
示例 3：
输入：s = "))(("
输出：""
解释：空字符串也是有效的
示例 4：
输入：s = "(a(b(c)d)"
输出："a(b(c)d)"
"""
class Solution:
    def minRemoveToMakeValid(self, s: str):
        stack = []
        flag = []
        result =[]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    flag.append(i)
            else:
                continue
        # 加入多余的左括号的索引
        while stack:
            flag.append(stack.pop())
        for i in range(len(s)):
            if i not in flag:
                result.append(s[i])
            else:
                continue
        result = ''.join(result)
        return result
solution = Solution()
result = solution.minRemoveToMakeValid("lee(t(c)o)de)")
print(result)






