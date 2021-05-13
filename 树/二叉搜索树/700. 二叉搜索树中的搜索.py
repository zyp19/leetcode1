"""700. 二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
方法1：通过中序遍历来找
"""
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        res = []
        res = self.traverse(root,res)
        for _ in res:
            if _.val==val:
                return _
        else:
            return None
    def traverse(self, root: TreeNode,res):
        if not root:
            return []
        # 下面这三行也可以写成 res = self.traverse(root.left,res)+[root]+self.traverse(root.right,res)
        self.traverse(root.left,res)
        res += [root]
        # 上一行也可以写成res.append(root)
        self.traverse(root.right,res)
        return res
"""
方法2：通过二分查找来找
"""
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if val < root.val:
            return self.searchBST(root.left,val)
        elif val > root.val:
            return self.searchBST(root.right,val)
        else:
            return root