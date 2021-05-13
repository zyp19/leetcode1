"""701. 二叉搜索树中的插入操作
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。返回插入后二叉搜索树的根节点。输入数据保证新值和原始二叉搜索树中的
任意节点值都不同。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果 。
"""
"""
这道题我想的有点多，我想的是找到一个位置把结点放进去，然后需要类似链表插入的方式（意思就是要把结点放在两个现有结点之间），但其实不用这样，
只要找到一个合适的叶子结点即可。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 关于返回值的问题，如果是像22行这样的获取每一个结点的值，最后还返回root，说明是返回整棵树，如果不在22行获取每一个结点的值，而是直接写return self.insertIntoBST,也是返回到根节点即整棵子树
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val = val)
        if root.val > val:
            root.left =  self.insertIntoBST(root.left,val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        return root
    # 错误原因，每个if都有返回值，如果28行直接满足条件就走了，哪种可以呢？就是最终的return值是调用自身函数的才可以在特殊值里return
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val = val)
        if root.val > val:
            return self.insertIntoBST(root.left,val)
        if root.val < val:
            return self.insertIntoBST(root.right,val)
"""
从这正确和错误的问题中可以总结一下二叉搜索树中”找“框架
"""
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
        #     找到插入位置
            return TreeNode(val=val)
        # 去左子树找
        if root.val > val:
            root.left =  self.insertIntoBST(root.left,val)
        #     去右子树找
        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        # 返回根节点（即这棵树）
        return root