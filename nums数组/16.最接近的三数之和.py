"""16. 最接近的三数之和
给定一个包括n个整数的数组nums和一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""
"""
target与result的差绝对值最小
"""
from typing import List
class Solution():
    def threeSumClosest(self, nums: List[int], target: int):
        n = len(nums)
        res = float('inf')
        if not nums or n < 3:
            return []
        # 排序的作用：1.排除相关重复元素 2.
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l<r:
                # 得到三数之和，和当前的res进行比较，如果当前和与target之差较小的话，那么就记住新的这个值
                a = nums[i]+nums[l]+nums[r]
                if abs(target-a) < res:
                    res = abs(target-a)
                    sum = a
                    # 假设每组输入只存在唯一答案，即不用去重的意思
                    # 用左右指针去找条件符合的元素时，一定要加上l<r保证左指针在右指针前面，和快速排序一个道理。
                    # while l<r and nums[l] == nums[l+1]:
                    #     l = l+1
                    # while l<r and nums[r] ==nums[r-1]:
                    #     r = r-1
                #     进行下一情况的选择，也就是左右指针的移动，移动的过程中要注意把所有的情况都包括在内。
                # 过了测试用例89/131个测试用例，原因是双指针同时移动是遗漏情况的，必须是左右指针分别进行移动：
                # else:
                #     l += 1
                #     r -= 1
                if a == target:
                    return target
                elif a < target:
                    l += 1
                else:
                    r -= 1
        return sum
solution = Solution()
result = solution.threeSumClosest(nums = [1,2,4,8,16,32,64,128], target = 82)
print(result)



