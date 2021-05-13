from typing import List
import numpy as np
# 思路是设置一个self.left，找到target出现的特定列，然后再沿着列去寻找。
# 这种做法设置一个全局的self.left是不对的，如果查找的数比第一维的所有数都大，那self.left势必会等于len(array[0])，这样并不能起到self.left的作用。
class Solution_1:
    # array 二维列表
    def __init__(self):
        self.left =0
    def Find(self, target, array:List[List[int]]):
        mid = self.binarySearch(array[0],target)
        if mid == -1:
            a = np.array(array)
            b = a[0:, self.left - 1]
            self.left = 0
            result = self.binarySearch(b, target)
            if result ==-1:
                return False
            else:
                return True
        else:
            return True
    def binarySearch(self,nums,target):
        right = len(nums)-1
        while self.left <= right:
            mid = int(self.left+(right-self.left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                self.left = mid + 1
            elif nums[mid]>target:
                right = mid - 1
        return -1


class Solution:
    # array 二维列表
    def Find(self, target, array:List[List[int]]):
        left =0
        def binarySearch(nums,target):
            nonlocal left
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = int(left+(right-left)/2)
                if nums[mid] == target:
                    return mid
                elif nums[mid]<target:
                    left = mid + 1
                elif nums[mid]>target:
                    right = mid - 1
            return -1
        mid = binarySearch(array[0],target)
        if mid == -1:
            a = np.array(array)
            b = a[0:, left - 1]
            left = 0
            result = binarySearch(b, target)
            if result ==-1:
                return False
            else:
                return True
        else:
            return True

s = Solution()
print(s.Find(19,[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
