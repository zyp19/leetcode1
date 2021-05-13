"""230.二叉树搜索树中第k小的元素
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
"""
# Definition for a binary tree node.
"""
关于每次递归得到的返回值的研究问题：
1.如果递归的这个函数有返回值，那么每次调用子树的时候需要将返回值赋给一个变量以接受该返回值（！！！！）
2.需要一个列表list或一个字符串str将每次子树输出的值都保存到该列表或字符串时，可以直接return 递归函数（左子树）+根+递归函数（右子树）
3.需要一个列表list或一个字符串str将每次子树输出的值都保存到该列表或字符串时，可以在递归函数中创建一个该变量，然后将左子树的结果和右子树的结果和根加到一起
res += self.inorder(root.left)+[root.val]+self.inorder(root.right)
T652.寻找重复的子树（）
res += traverse(root.left, counter) + traverse(root.right, counter)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = self.inorder(root)
        return self.res[k-1]
    def inorder(self,root:TreeNode):
        if not root:
            return []
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
        return self.res

s = Solution()
t1 = TreeNode(3,TreeNode(1,None,TreeNode(2)),TreeNode(4))
print(s.kthSmallest(t1,1))

class Solution_1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = self.inorder(root)
        return res[k-1]
    def inorder(self,root:TreeNode):
        res = []
        if not root:
            return []
        res += self.inorder(root.left)+[root.val]+self.inorder(root.right)
        return res

s = Solution_1()
t1 = TreeNode(3,TreeNode(1,None,TreeNode(2)),TreeNode(4))
print(s.kthSmallest(t1,1))


class Solution_3:
    def kthSmallest(self, root, k):

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]

# 将每一次左子树和右子树和根的结果加在一起，如同这个中序遍历
