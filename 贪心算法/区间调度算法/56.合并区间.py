"""56.合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，
该数组需恰好覆盖输入中的所有区间。
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        # 将活动按照end升序排列
        def takeEnd(e):
            return e[1]
        intervals.sort(key=takeEnd)
        res = []
        x_end = intervals[0][1]
        x_s = intervals[0][0]
        for i in range(1,len(intervals)):
            # 当前活动的开始时间比上一个活动的结束时间靠后
            start = intervals[i][0]
            if start<=x_end:
                res.append([x_s,intervals[i][1]])
                x_end = intervals[i][1]
                x_s = intervals[i][0]
            elif len(res) == 0:
                res.append([x_s,x_end])
                res.append(intervals[i])
            else:
                res.append(intervals[i])
        return res
s = Solution()
print(s.merge([[1,4],[5,6]]))
"""经验：区间类的问题，一般而言是需要画图思考的。因为只有建立直观的感觉，才能更有效的去思考解决问题的方案。
还有需要画图思考的相关算法问题有（其实绝大部分都需要打草稿，大神除外）：
和物理现象相关的：第 42 题：接雨水问题、第 11 题：盛最多水的容器、第 218 题：天际线问题；
本身问题描述就和图形相关的问题：第 84 题：柱状图中最大的矩形；
链表问题：穿针引线如果不画图容易把自己绕晕；
回溯算法问题：根据示例画图发现每一步的选择和剪枝的条件；
动态规划问题：画示意图发现最优子结构。"""
"""
画图之后，可以看出，可以合并的区间是有交集的区间。
"""
class Solution(object):
    def merge(self, intervals):
        if len(intervals)==0:
            return intervals
        list1 = []
        intervals=sorted(intervals,key = lambda x:x[0])
        list1.append(intervals[0])
        for i in intervals:
            # intervals中的元素的start大于list中最后一个元素的end就一定没有交集，就把i对应的数组放到list中
            if i[0] > list1[-1][1]:
                list1.append(i)
            # 有交集的情况下，如果说intervals中的元素的end大于list最有一个元素的end，就把右端点写成intervals的end
            else: #这里本来之间elif就好，但是为了方便理解。
                if i[1] > list1[-1][1]:
                    list1[-1]=[list1[-1][0],i[1]]
        return list1
s = Solution()
print(s.merge([[1,3],[1,5],[6,9]]))