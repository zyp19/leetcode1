"""435.无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。注意:可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1输入: [ [1,2], [2,3], [3,4], [1,3] ]输出: 1解释: 移除 [1,3] 后，剩下的区间没有重叠。
"""
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x:x[1])
        count = 1
        x_end = intervals[0][1]
        for inter in intervals:
            # 有交集
            if inter[0] >= x_end:
                count += 1
                x_end = inter[1]
        return len(intervals)-count
s = Solution()
print(s.eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]))
