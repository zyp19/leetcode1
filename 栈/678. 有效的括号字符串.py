"""678. 有效的括号字符串（第一遍没有做出来的）
给定一个只包含三种字符的字符串：（，）和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
1.任何左括号 (必须有相应的右括号 )。
2.任何右括号 )必须有相应的左括号 (。
3.左括号 ( 必须在对应的右括号之前 )。
4.*可以被视为单个右括号 )，或单个左括号 (，或一个空字符串。
5.一个空字符串也被视为有效字符串。
"""
class Solution:
    def checkValidString(self, s: str) :
        stack_left, stack_star = [], []
        for i in range(len(s)):
            # 左括号//星号 都分别入栈
            if s[i] == '(':
                stack_left.append(i)
            elif s[i] == '*':
                stack_star.append(i)
            # 如果遇到右括号
            elif s[i] == ')':
                # 如果有尚未匹配左括号 先与栈顶的左括号匹配
                if stack_left:
                    stack_left.pop()
                # 如果有尚未消耗的星号 则变身左括号与s[i]匹配 (出栈)
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        # 这时候所有的右括号已经匹配完毕，而且在左括号的对应的栈中还有东西时，如果说星栈中还有星且星星的个数多于左括号栈中括号的数量的话，
        # 就可以完成遗留在栈中的左括号和星的匹配。
        # stack_left非空 也可能有效 只要满足for any左括号, there exist a 右侧的'*'(index更大)
        # 因为越靠近栈顶index越大 只需判断栈顶'*' 当栈顶的'*'的ind大于当前左括号ind的时候弹出
        while stack_left:
            if not stack_star:
                return False  # 无*匹配
            elif stack_left[-1] > stack_star[-1]:
                return False  # 无右侧*匹配
            else:
                stack_left.pop()
                stack_star.pop()
        return True
solution = Solution()
solution.checkValidString("(((*****)")