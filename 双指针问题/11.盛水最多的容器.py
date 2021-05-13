"""11.盛水最多的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        max_area = float("-inf")
        while left < right:
            a = height[left]
            b = height[right]
            area = min(a , b)*(right - left)
            if area > max_area:
                max_area = area
            left += 1
            right -= 1
            # 下一个柱子短，直接放弃这个柱子
            if height[left] < a and height[right] < b:
                left +=1
                right-=1
            elif height[left]<a:
                left -= 1
            elif height[right]<b:
                right += 1
        return max_area
s = Solution()
print(s.maxArea([1,2,4,3]))

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res