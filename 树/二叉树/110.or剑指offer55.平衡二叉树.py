"""110 or 剑指offer55 平衡二叉树（单数 构造辅助函数 后序（自顶向下递归 自底向上求解真的牛逼）/先序 返回值就是对每颗子树的判断结果）
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    # 使用递归的方法自顶向下求解：
    # 可以说是 自底向上 判断树的高度，但当树平衡时，仍无法避免重复判断的问题，就是有重复子问题，重复子问题在于and后面的Balanecd调用depth时，要重新计算一遍高度
    def isBalanced_1(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced_1(root.left) and self.isBalanced_1(root.right)

    def depth_1(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    # 5.26自己尝试
    def test(self,root):
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right))<=1:
            # 导致重复子问题。因此自己写的这个test()方法也属于是自顶向下的方法
            if self.test(root.left) and self.test(root.right):
                return True
            else:
                return False
        else:
            return False
    def height(self,root):
        if root is None:
            return 0
        else:
            l1 = self.height(root.left)+1
            l2 = self.height(root.right)+1
            if l1>l2:
                return l1
            else:
                return l2

