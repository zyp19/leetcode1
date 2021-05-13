"""543.二叉树的直径（这道题真的很妙，通过左右子树之和来计算两个结点的路径的长度，通过引入一个max记录当前的最大的结点路径长度 想不到 需要多看看）
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
注意：两结点之间的路径长度是以它们之间边的数目表示。
"""
"""
最大深度：从根节点到叶节点最长的那条路径 上的节点数。最大路径：任意两个节点最长的那条路径 上的边数。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.max
    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        '''每个结点都要去判断左子树+右子树的高度是否大于self.max，更新最大值，每个节点都要保存'''
        self.max = max(self.max, l + r)
        # 返回的是高度
        return max(l, r) + 1
# h不应该设在biLength中
class biLength:
    def biLength(self,root):
        if not root:
            return 0
        h = 0
        h = max(h,self.height(root))
        return h
    def height(self,root:TreeNode):
        if not root:
            return 0
        return self.height(root.left)+self.height(root.right)




