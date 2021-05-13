"""活动选择问题：今天有好几个活动，每个活动都可以用区间[start,end]表示开始和结束的时间，问今天能参加的最大活动的个数。
"""
from typing import List
class Solution:
    def intervalSchedule(self,intvs:List[List]):
        if len(intvs) == 0:
            return 0
        # 将活动按照end升序排列
        def takeEnd(e):
            return e[1]
        intvs.sort(key=takeEnd)
        print(intvs)
        # 记录参加的最大活动的个数
        count = 1
        x_end = intvs[0][1]
        for i in range(len(intvs)):
            # 当前活动的开始时间比上一个活动的结束时间靠后
            start = intvs[i][0]
            if start>=x_end:
                count += 1
                x_end = intvs[i][1]
        return count
s = Solution()
print(s.intervalSchedule([[1,2],[2,3],[3,4],[1,3]]))