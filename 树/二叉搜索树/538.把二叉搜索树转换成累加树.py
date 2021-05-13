"""538.把二叉搜索树转换成累加树
给出二叉搜索树的根节点，该树的节点值各不相同，请你将其转换为累加树，使每个节点node的新值等于原树中 大于或等于node.val的值 之和。
提醒一下，二叉搜索树满足下列约束条件：
节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
"""
"""
逆序的中序遍历：因此是右子树根节点左子树这样的遍历顺序，而每个结点的值等于它的先前遍历的所有结点的累加值，所以需要在递归函数外维护一个全局变量
保存每个结点的累加值。

简单总结下吧，BST 相关的问题，要么利用 BST 左小右大的特性提升算法效率，要么利用中序遍历的特性满足题目的要求，也就这么些事儿吧。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.convertBST(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convertBST(root.left)
        return root
s = Solution()
# [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
t1 = TreeNode(4,TreeNode(1,TreeNode(0),TreeNode(2,None,TreeNode(3))),TreeNode(6,TreeNode(5),TreeNode(7,None,TreeNode(8))))
s.convertBST(t1)
