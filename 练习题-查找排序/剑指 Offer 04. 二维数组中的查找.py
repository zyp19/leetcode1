"""剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个
二维数组和一个整数，判断数组中是否含有该整数。
示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target=5，返回true。
给定target=20，返回false。
"""
from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int):
        for li in matrix:
            l,r = 0,len(li)-1
            while l<=r:
                mid = (l+r)//2
                if target == li[mid]:
                    return True
                elif target > li[mid]:
                    l = mid+1
                else:
                    r = mid-1
        return False
solution = Solution()
res = solution.findNumberIn2DArray(matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],target=5)
print(res)
