"""450.删除二叉树中的结点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的key对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的
根节点的引用。一般来说，删除节点可分为两个步骤：首先找到需要删除的节点；如果找到了，删除它。
说明： 要求算法时间复杂度为O(h)，h 为树的高度。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    找到目标节点了，比方说是节点A，如何删除这个节点，这是难点。因为删除节点的同时不能破坏 BST 的性质。有三种情况
    """
    # 又犯了错误。就是return值的问题，第一个if算是特殊值，在这里面return就是直接return
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root.val == key:
            # 情况1：左右孩子都没有
            if not root.left and not root.right:
                return None
            # 情况2：只有一个左孩子或一个右孩子
            elif not root.left or not root.right:
                return root.left or root.right
            # 情况3：左孩子和右孩子都有
            elif root.left and root.right:
                min = self.delete(root.right)
                root.val = min.val
                return self.deleteNode(root.right, min.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        return root

    def delete(self, root: TreeNode):
        while root.left:
            root = root.left
        return root
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val == key:
            # 情况2：只有一个左孩子或一个右孩子
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # 情况3：左孩子和右孩子都有
            elif root.left and root.right:
                min = self.delete(root.right)
                root.val = min.val
                root.right = self.deleteNode(root.right, min.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

    def delete(self, root: TreeNode):
        while root.left:
            root = root.left
        return root


