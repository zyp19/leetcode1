"""100.相同的树（双树 无辅助函数 判断 先序遍历 返回值是判断左右子树）
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 判断题用先序遍历挺好用的（226 965 110 101）
    # 改变树的结构用后序遍历挺好的用的（226 617）
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p or not q:
            return not p and not q
        elif p.val != q.val:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)




