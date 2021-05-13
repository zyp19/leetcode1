"""剑指offer27.二叉树的镜像/226.翻转二叉树（单树 改变树结构 典型的后、先序遍历 返回值是得到新子树的根（表明子树已经翻转了））
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 思路：第二层是左右孩子交换，从第三层开始，自己的左孩子和兄弟结点的右孩子交换，自己的右孩子和兄弟结点的左孩子交换
# 后序遍历官方答案
class Post_Solution:
    def mirrorTree(self, root: Node) :
        if not root:
            return None
        # 递归把每一个根节点的两个子树交换，本质上就是一个后序遍历
        # 交换两个子树真的很厉害
        root.left = self.mirrorTree(root.left)
        root.right = self.mirrorTree(root.right)
        root.left, root.right = root.right, root.left
        return root
# 先序遍历的结果，为什么到了叶子节点的时候整个函数不会返回，因为函数栈还没有结束，所以并不能中途截断，只能返回到调用它的上一级节点。
class Pre_Solution:
    def mirrorTree_1(self, root: Node):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        # 前序遍历改变一棵树时很奇怪，这里为啥不需要得到左右子树的返回值呢
        # 答案是最好写上，这个题不存在给每个子树（每个节点赋值，二617合并二叉树需要给每个节点赋值）
        self.mirrorTree_1(root.left)
        self.mirrorTree_1(root.right)
        return root