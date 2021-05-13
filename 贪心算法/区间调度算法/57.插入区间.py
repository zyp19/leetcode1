"""57.插入区间
给出一个无重叠的 ，按照区间起始端点排序的区间列表。在列表中插入一个新的区间，你需要确保列表中的区间仍然 有序且不重叠（如果有必要的话，可以 合并区间）。
示例 1:：
输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
解释: 新区间[2,5] 与 [1,3]重叠，因此合并成为 [1,5]。
示例 2:：
输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 新区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠，因此合并成为 [3,10]。
"""
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals,key=lambda x:x[0])
        li = []
        li.append(intervals[0])
        for inter in intervals:
            if inter[0] > li[-1][1]:
                li.append(inter)
            else:
                if inter[1] > li[-1][1]:
                    # 要强烈注意这样写是错误的，跟下一句的放在一起体会一下
                    # li.append([li[-1][0],inter[1]])、
                    # 走一步else-if的原因是势必要合并，那之前的li[-1][1]一定要被覆盖才可以，所以选择了赋值，而不是append
                    li[-1] = [li[-1][0], inter[1]]
        return li

