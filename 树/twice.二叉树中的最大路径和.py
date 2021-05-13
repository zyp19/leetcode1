"""124.二叉树中的最大路径和
给定一个非空二叉树,任意选择两个节点(可以是同一个节点),两个节点必然可以通过唯一的一个路径连接,计算该路径上所有节点(包括这两个节点)的val值和.
返回其中的最大值.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode)-> int:
