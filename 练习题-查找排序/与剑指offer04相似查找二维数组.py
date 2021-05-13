"""剑指 Offer 04相似的一道题. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一行的第一个数比上一个大。请完成一个高效的函数，输入这样的一个
二维数组和一个整数，判断数组中是否含有该整数。
示例:
现有矩阵 matrix 如下：
[
  [1,  3,  5,   7],
  [10, 11,  16, 20],
  [23, 30,  34, 50],
]
给定 target=3，返回true。
给定target=20，返回false。
"""
# 这个二维数组实际上是一个有序的数组，可以考虑使用二分查找来做。难点在于是二维数组，二分查找的中间元素的下标需要确定一下。
# mid = (i + j) // 2
# m = mid // w
# n = mid % w
from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int):
        i = 0
        w = len(matrix)
        h = len(matrix[0])
        j = w*h - 1
        # 核心代码是快速排序
        while i <= j:
            mid = (i+j)//2
            m = mid // w
            n = mid % w
            if target == matrix[m][n]:
                return True
            elif target < matrix[m][n]:
                j = mid-1
            else:
                i = mid+1
        return False
solution = Solution()
result = solution.findNumberIn2DArray(matrix = [
  [1,  3,  5,   7],
  [10, 11,  16, 20],
  [23, 30,  34, 50],
], target=3)
print(result)