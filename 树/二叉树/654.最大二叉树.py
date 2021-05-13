"""654.最大二叉树
给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：
二叉树的根是数组 nums 中的最大元素。
左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
返回有给定数组 nums 构建的 最大二叉树。
"""
# Definition for a binary tree node.
"""
构造子树的问题，关键是要把一颗子树的起始位置和终止位置搞明白
"""
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:
            return None
        max = self.findMax(nums)
        root = TreeNode(nums[max])
        # 这种写法是每次都改变nums这个数组中的内容，相当于是完成了数组的一次赋值。
        root.left = self.constructMaximumBinaryTree(nums[0:max])
        root.right = self.constructMaximumBinaryTree(nums[max+1:len(nums)])
        return root

    # 寻找最大值的下标
    def findMax(self,nums):
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[j] <= nums[i]:
                    j += 1
                else:
                    i = j
            return i

s = Solution()
print(s.constructMaximumBinaryTree([3,2,1,6,0,5]))

# 比我写的更清晰的写法，我写的方法也对，但是数组下标容易搞不清楚，而且“比较大小的这个函数”也没必要拿出来，
def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
    return traversal(nums, 0, len(nums))

def traversal(nums, left, right):
        if left >= right:
            return None
        maxValueIndex = left
        # 比较大小不需要用双指针比较
        for i in range(left + 1, right):
            if nums[i] > nums[maxValueIndex]:
                maxValueIndex = i
        root = TreeNode(nums[maxValueIndex])
        # nums的还是全数组，但是只取切片部分传参
        root.left = traversal(nums, left, maxValueIndex)
        root.right = traversal(nums, maxValueIndex + 1, right)
        return root
