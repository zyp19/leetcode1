"""965.单值二叉树（典型的先序遍历）
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。
"""
"""
前序遍历模板：看下根节点要干嘛，当前根节点操作完之后，然后根据函数的定义让左右孩子做同样的事情。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: TreeNode):
        if not root:
            return True
        # 妙：左右子树有可能不存在而且三个数互相比较，只需要两两比较就可以
        # 纯前序遍历，先判断根节点，再走左右孩子
        if root.right and root.val != root.right.val or root.left and root.val != root.left.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


