"""
题目要求：给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 0， 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

思路：
做题中出现过一次题目理解中的错误：不是这三个数之间不能有重复的数，而是这三个数总体来说不能和另外的三个数相等。
"""

class Solution:
    def threeSum(self, nums):

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        for i in range(n-2):
            if (nums[i] > 0):
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    # 注意这里是将数组加入到二维数组当中
                    res.append([nums[i], nums[L], nums[R]])
                    # 判断L、R能不能重复是为了来避免出现两个三元组重复的情况！！！
                    # 这一步是判断l、r为下标的值到底能不能重复呢,不管有没有重复的值都要进行l=l+1,r=r+1的操作，如果有重复的值，说明这个值不能用了，相当于+2
                    # 没有重复的值就直接+1，相当于判断下一个是否可用，R为同理。
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                #     三数之和小于0的话，只能去调整L值，因为R位置对应的数组值已经是最大的了，所以只能来增加L相对应的数组值。
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

if __name__ == '__main__':
    enstance = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    new_nums=[]
    new_nums=enstance.threeSum(nums)
    print(new_nums)








