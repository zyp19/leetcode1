"""844.比较含退格的字符串
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。
"""
# 方法1：使用栈
# 因为是要将#和#前面的字符删掉，可以使用栈，这个代码写得真是优雅！
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s: str) -> str:
            ret = list()
            for ch in s:
                if ch != "#":
                    ret.append(ch)
                elif ret:
                    ret.pop()
            # list转str
            return "".join(ret)

        return build(S) == build(T)

s = Solution()
s.backspaceCompare(S = "ab#c", T = "ad#c")
# 如果不能使用栈，即要求是0(1)的空间复杂度：
# 方法2：双指针法
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                #  普通字符
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                #  普通字符
                # 只有普通字符需要比较，所以这里需要break,进入下面的地方进行比较
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            #     有一个字符串结束了
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True


