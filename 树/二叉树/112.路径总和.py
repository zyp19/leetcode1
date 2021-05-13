"""112.路经总和
给你二叉树的根节点root和一个表示目标和的整数targetSum，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和targetSum 。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return
        l = self.hasPathSum(root.left,targetSum)
        r = self.hasPathSum(root.right,targetSum)
        if l + root.val == targetSum or l+root
        return h
