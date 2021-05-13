"""1541. 平衡括号字符串的最少插入次数
给你一个括号字符串s，它只包含字符'(' 和')'。一个括号字符串被称为平衡的当它满足：
任何左括号'('必须对应两个连续的右括号'))'。
左括号'('必须在对应的连续两个右括号'))'之前。
比方说"())"，"())(())))" 和"(())())))"都是平衡的，")()"，"()))" 和"(()))"都是不平衡的。
你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。
请你返回让 s平衡的最少插入次数。
"""
class Solution:
    def minInsertions(self, s: str):
        stack = []
        nums = 0
        i = 1
        while i <= len(s):
            if s[i-1] == '(':
                stack.append(s[i-1])
                i += 1
            elif s[i-1] == ')':
                if i == len(s):
                    if stack:
                        stack.pop()
                        nums += 1
                    else:
                        nums += 2
                    i += 1
                elif s[i] == ')':
                    if stack:
                        stack.pop()
                    else:
                       nums += 1
                    i += 2
                elif  s[i] != ')':
                    if stack:
                        stack.pop()
                        nums += 1
                    else:
                       nums += 2
                    i += 1
        if stack:
            nums += len(stack)*2
        return nums
solution = Solution()
nums = solution.minInsertions("))))))((()))(()(()))")
# nums = solution.minInsertions("(((((((((()")
print(nums)


