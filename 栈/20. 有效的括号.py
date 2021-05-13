"""20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""
"""
细节问题：
要注意挺多东西的，很多细节问题没有注意到：
1.for i in rang(len(s)):
规定一下，如果是遍历字符串、数组使用for i in range (len(s))，如果是遍历链表一般用while p:这样的循环条件
2.如果是遍历数组、字符串、列表、元组等这样顺寻存储的数据结构，不要出现[i+1]这种下标，原因是会产生下表越界的问题
3.栈实际上是由列表实现的，因此使用的是链表中的方法
思路问题：
1.要保证”遇到左括号就入栈，遇到右括号就判断“以此规则来构造一个字典，因此右括号要作为字典的key，这样才能拿字典的value和栈顶元素进行比较，
要将左括号作为字典的value，这样判断key是否在字典中时，左括号一定是不作为key存在于字典中的，因此左括号可以尽情入栈。
2.遍历晚完个字符串之后呢，如果说括号全部都能匹配的话，此时栈一定是空的，因为右括号不入栈，左括号入栈。
"""
class Solution:
    def isValid(self, s:str) :
        if len(s) % 2 == 1:
            return False
        stack =[]
        dict ={')':'(','}':'{',']':'['}
        for i in range(len(s)):
            if s[i] in dict and stack:
                if dict[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        #         return stack == [] 的意思一样，返回一个布尔值：当栈为空时返回 True， 否则返回 False
        return not stack
solution = Solution()
flag = solution.isValid("{([)}")
print(flag)