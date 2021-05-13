# Definition for a binary tree node.
# 6.11做发现问题：左右子树的深度不超过1，为什么要求最大深度呢，我不明白！！！！原来是树的深度（高度）的定义就是树中结点的最大层数!!
# 自顶向下
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.left)-self.height(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right))+1

# 自底向上,没有想到
class Solution:
    # 后序遍历模板，使用递归的方法自底向上求解,自顶而下递归,然后自底向上处理：
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1
    def recur(self, root):
        if not root:
            return 0
        left = self.recur(root.left)
        if left == -1:
            return -1
        right = self.recur(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1