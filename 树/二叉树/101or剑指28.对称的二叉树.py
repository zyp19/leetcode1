"""剑指offer28.对称的二叉树（双树问题 判断 ）
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
"""
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 递归栈中的数据返回调用者 和 每一层数据被函数调用的函数返回值如何处理
# 函数的返回值是返回到调用者处
# 错误答案，这种做法是计算子树是否相等，但是不能计算堂兄弟节点（即它们的父亲节点是同一个父亲）的值是不是相同。
# 需要构造辅助函数。这类题目通常只用根节点子树对称性无法完全解决问题，必须要用到子树的某一部分进行递归，即要调用辅助函数比较两个部分子树。
# 形式上主函数参数列表只有一个根节点，辅助函数参数列表有两个节点。
# class Solution:
#     # 前序遍历
#     def isSymmetric(self, root: Node):
#         if root.left == None and root.right == None:
#             return True
#         if root.left == None or root.right == None:
#             return False
#         if root.left.val != root.right.val:
#             return False
#         return self.isSymmetric(root.left) and self.isSymmetric(root.right)
# solution = Solution()
# tree = Node(1, Node(2, Node(3), Node(4)),Node(2, Node(4), Node(3)))
# print(solution.isSymmetric(tree))

class Recur:
    def isSymmetric(self, root: Node):
        if not root:
            return True
        else:
            return self.check(root.left,root.right)

    def check(self,node1,node2):
        if node1 and node2 and node1.val == node2.val:
            return self.check(node1.left,node2.right) and self.check(node1.right,node2.left)
        if node1 and node2 and node1.val != node2.val:
            return False
        # 这两行可以优化一下，改成：
        # if not node1 or not node2:
        #    return not node1 and not node2
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
r = Recur()
tree = Node(1, Node(2, 3))
print(r.isSymmetric(tree))




