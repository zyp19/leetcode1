class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removes = [-1]
        l_paren = []
        for i in range(len(s)):
            if s[i] == '(':
                l_paren.append(i)
            elif s[i] == ')':
                if len(l_paren) == 0:
                    removes.append(i)
                else:
                    l_paren.pop()
        removes = removes + l_paren + [len(s) + 1]
        # 我是真没看懂这块是啥意思。。。
        ans = []
        for idx in range(len(removes) - 1):
            ans += s[removes[idx] + 1 : removes[idx + 1]]
        return ''.join(ans)
solution = Solution()
a = solution.minRemoveToMakeValid("(a(b(c)d)")
print(a)
