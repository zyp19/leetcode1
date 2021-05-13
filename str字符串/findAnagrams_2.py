from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str):
        flag,target = defaultdict(int),defaultdict(int)
        for c in p: target[c] +=1
        i, j, l, num = 0, 0, len(p), 0
        res = []
        while j < len(s):
            if s[j] not in target:
                flag = defaultdict(int)
                i, j = j + 1, j + 1
                num = 0
            else:
                while flag[s[j]]==target[s[j]]:
                    flag[s[i]] -= 1
                    num -= 1
                    i = i + 1
                flag[s[j]]  +=1
                num += 1
                j += 1
                if num == l: res.append(i)
        return res
solution = Solution()
res = solution.findAnagrams("cbaebabacd","abc")
print(res)