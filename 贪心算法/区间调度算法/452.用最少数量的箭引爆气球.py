"""452.用最少数量的箭引爆气球
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，
因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，
若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足 xstart≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。
弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
"""
"""
实际上，是求解最大不相交子集的个数，因为相交子集的气球都可以被射中。
"""
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorted函数取二维数组中的可迭代元素，即每一个元素
        points = sorted(points,key = lambda x:x[1])
        x_end = points[0][1]
        count=1
        for p in points:
            # 不相交
            if p[0] > x_end:
                count += 1
                x_end = p[1]
        return count