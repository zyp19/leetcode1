"""165.比较版本号
给你两个版本号 version1 和 version2 ，请你比较它们。
版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。
比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。
规则如下：如果version1>version2返回1，如果version1<version2 返回 -1，除此之外返回 0。
示例 1：
输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # version1 = "1.01"
        #  version1.split(".")->['1','01']
        #  list(map(int,version1.split(".")))->[1,1]
        li1 = list(map(int,version1.split(".")))
        li2 = list(map(int,version2.split(".")))
        # print(li1,li2)
        i,j = 0, 0
        while i < len(li1) and j <len(li2):
            if li1[i] < li2[j]:
                return -1
            elif li1[i] > li2[j]:
                return 1
            i += 1
            j += 1
        if i == len(li1) and j == len(li2):
            return 0
        else:
            while i < len(li1):
                if li1[i] == 0:
                    if i == len(li1)-1:
                        return 0
                    i += 1
                    continue
                else:
                    return 1
            while j < len(li2):
                if li2[j] == 0:
                    if j == len(li2)-1:
                        return 0
                    j += 1
                    continue
                else:
                    return -1

s = Solution()
print(s.compareVersion(version1 = "1.0", version2 = "1"))
# 方法1：
# 根据点将字符串分割，并把分割的结果存到一个数组中。
# 遍历两个字符串，其中给先结束的字符串填0，以能够继续比较。
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        li1 = version1.split(".")
        li2 = version2.split(".")
        n1,n2 = len(li1),len(li2)
        for i in range(max(n1,n2)):
            # 这里为字符串补0的操作值得学习
            i1 = int(li1[i]) if i < n1 else 0
            i2 = int(li2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1>i2 else -1
        return 0
# 方法2：要求不能使用split()函数，即不能使用额外的空间存储转换后的字符
# 根据该要求，使用“双指针”的方法，核心思路就是遍历两个字符串，截取“.”之间的数字进行比较
class Solution_1:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        while p1 < n1 or p2 < n2:
            chunk1, p1 = self.get_next_chunk(version1, p1, n1)
            chunk2, p2 = self.get_next_chunk(version2, p2, n2)
            if chunk1 != chunk2:
                return 1 if chunk1 > chunk2 else -1
        return 0
    def get_next_chunk(self, version, p, n):
        if p >= n:
            return 0, p
        end = p
        while end < len(version) and version[end] != '.':
            end += 1
        chunk = int(version[p:end])
        return chunk, end + 1
s1 = Solution_1()
print(s1.compareVersion(version1 = "1.0.1", version2 = "1.0.0"))