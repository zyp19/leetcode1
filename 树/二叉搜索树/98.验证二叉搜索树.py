"""※98.验证二叉搜索树※
给定一个二叉树，判断其是否是一个有效的二叉搜索树。假设一个二叉搜索树具有如下特征：节点的左子树只包含小于当前节点的数。节点的右子树只包含大于
当前节点的数。所有左子树和右子树自身必须也是二叉搜索树。
"""
"""
本题展示了一种错误解法和一种正确解法，错误解法是只能够来判断当前结点的左右子树能够符合题意，但是不能够满足上一层的根节点比它的所有左子树和右子树的题意
所以需要传参。我们通过使用辅助函数，增加函数参数列表，在参数中携带额外信息，将这种约束传递给子树的所有节点，这也是二叉树算法的一个小技巧吧。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 错误解法，只比较了当前结点的子树情况，没考虑到上层结点对应的子树情况
# 出现问题的原因在于，对于每一个节点root，代码值检查了它的左右孩子节点是否符合左小右大的原则；但是根据 BST 的定义，root的整个左子树都要小于root.val，
# 整个右子树都要大于root.val。
class Solution_false:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.val < root.left.val:
            return False
        if root.right and root.val > root.right.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
"""
正确方法1：传根节点的参数
"""
# 问题是，对于某一个节点root，他只能管得了自己的左右子节点，怎么把root的约束传递给左右子树呢？
# labuladong的做法是为根的右子树的左子树传入了一个参数min，因为只有右子树才会有min的位置的值的传入，左子树不会有，所以它会一直找到一颗给他传值
# 的祖父或曾祖父级别的结点，这个祖父或曾祖父一定是一个某个结点的右孩子，传的min=这个结点的root；
# 为左子树的右子树传入了一个参数max，用于定位它的祖父级别的结点，因为只有左子树才会传max值，所以一定会找到的这个祖父级别的或曾祖父级别的结点一定是
# 一个某个结点的左孩子，传的max= 这个结点的root。
class Solution_true1:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.traverse(root,None,None)
    def traverse(self,root:TreeNode,min:TreeNode,max:TreeNode):
        if not root:
            return True
        if min and min.val >= root.val:
            return False
        if max and max.val <= root.val:
            return False
        return self.traverse(root.left,min,root) and self.traverse(root.right,root,max)
"""
正确方法2：利用中序遍历的二叉搜索树是有序的这一特性，记录当前结点的值，判断当前结点是否大于前一个结点
"""
class Solution_true1:
    def __init__(self):
        self.pre = float("-inf")
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 判断题，中序遍历：先判断左子树满足条件吗，如果不满足，直接就返回
        if not self.isValidBST(root.left):
            return False
        # 每颗结点都要做的事情
        if root.val <= self.pre:
            return False
        self.pre = root.val
        # 再判断右子树是不是满足条件
        return self.isValidBST(root.right)


