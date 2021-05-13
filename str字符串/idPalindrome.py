"""9.回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
"""
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        s = str(x)
        j = len(s) - 1
        for i in range (j + 1):
            if i < j:
                if s[i] != s[j]:
                    return False
                if s[i] == s[j]:
                    j = j - 1
            else:
                return True
solution = Solution()
print(solution.isPalindrome(1001))


