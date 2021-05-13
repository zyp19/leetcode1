"""222.完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数
都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~2h个节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#  我的这种做法适用性比较广，二叉树可以，满二叉树也可以，时间复杂度为0(n)，空间复杂度为树的高度O(logN)，最坏为O(N)，时间复杂度为O（N）
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left)+self.countNodes(root.right)+1
# 下面先讲满二叉树如何计算结点个数，再讲完全二叉树的结点个数
    def fullTree(self,root:TreeNode):
        num = 0
        while root.left:
            root = root.left
            num += 1
        #     满二叉树的个数为2^h-1
        return pow(2,num)-1

# 完全二叉树比普通二叉树特殊，但又没有满二叉树那么特殊，计算它的节点总数，可以说是普通二叉树和完全二叉树的结合版
    def prefectTree(self,root:TreeNode):
        left_num,right_num = 0,0
        while root.left:
            root = root.left
            left_num += 1
        while root.right:
            root = root.right
            right_num += 1
        if left_num == right_num:
            return pow(2,left_num)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

