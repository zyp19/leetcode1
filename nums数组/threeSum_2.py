"""
题目要求：给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：给定数组 nums = [-1, 0, 0， 1, 2, -1, -4]，满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
双指针来解决这个问题，将数组从小到大排序
j=length-1初始化
1.遍历这个数组nums，找出nums[i]+nums[i+1]+nums[j]=0
2.if nums[i]+nums[i+1]+nums[j]>0:length-1前移
3.if nums[i]+nums[i+1]+nums[j]<0:i+1后移
4.if nums[i]==nums[i+1] continue
"""
class solution:
    def threeSums(self, nums):
        j = len(nums)-1
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if nums[i] == nums[i+1]:
                continue
            # 要使得整个数组的遍历的过程中i<j才行，因此要把下面三个都放在大循环中
            # if nums[i] + nums[i+1] + nums[j] == 0:
            #     result.append([[nums[i], nums[i+1], nums[j]]])
            # 这里用if是不对的，因为是想找到合适的i和j，因此一定要使用循环的！而且要注意左指针和右指针的边界问题，左指针绝对不能大于右指针
            # if nums[i] + nums[i+1] + nums[j] > 0:
            #     j = j - 1
            # if nums[i] + nums[i+1] + nums[j] < 0:
            #     i = i + 1
            # while(i < j & nums[i] + nums[i+1] + nums[j] > 0):
            #     j = j - 1
            # while (i < j & nums[i] + nums[i + 1] + nums[j] < 0):
            #     i = i + 1
            while i < j:
                if nums[i] + nums[i+1] + nums[j] == 0:
                    result.append([[nums[i], nums[i+1], nums[j]]])
                #     ! 这里没有想到要在这里去重，理由是：都找到一组了，就要去掉重复组，如果后续有和nums[i]或nums[j]重复的，都要去掉，而且while循环是保证了去除一些多次重复的数值
                    while i < j & nums[i] == nums[i+1]:
                        i = i + 1
                    while i < j & nums[j] == nums[i-1]:
                        j = j - 1
                if i < j & nums[i] + nums[i+1] + nums[j] > 0:
                    j = j - 1
                elif i < j & nums[i] + nums[i + 1] + nums[j] < 0:
                    i = i + 1
                i = i + 1
                j = j - 1

        return result

solution = solution()
result = []
result = solution.threeSums([-1, 2, 0, -3, 1, 6, -5])
print(result)

