"""111.二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#  方法1：dfs
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 需要注意下：当根节点的左右子树都没有时，会返回1：当根节点的左右子树只有1个时，根节点到叶子节点的最小高度选择左右子树高度最大的，因为另一颗子树不存在。
        if not root.left or not root.right:
            return max(self.minDepth(root.right),self.minDepth(root.left))+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
# 方法2：bfs
class Solution_1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = []
        q.append(root)
        height = 1
        while q:
            s = len(q)
            for i in range(s):
                cur = q.pop(0)
                if not cur.left and not cur.right:
                    return height
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
            height += 1
        return height