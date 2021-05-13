"""
二维数组转字典
"""
class Solution:
    def maxMatch(self , matchPairList ):
        flag ={}
        for i in range(len(matchPairList)):
            for j in range(1,len(matchPairList[0])):
                # 有人占了岗位
                if matchPairList[i][j-1] in flag.values() or matchPairList[i][j] in flag:
                    continue
                else:
                    flag[matchPairList[i][j]] = matchPairList[i][j-1]
        print(flag.values())
        return len(flag)

solution = Solution()
result = solution.maxMatch([[0,103],[1,103],[1,104],[2,104],[2,105],[2,106],[3,103]])
print(result)