"""剑指26.树的子结构（双树 有辅助函数 判断 前序遍历 返回值有点复杂的题（这里的返回值有点像平衡二叉树那道题）是判断三个地方 当前
节点能不能找到子结构 左右子树能不能找到子结构 如果有一个能就成功返回True 三个都不能就返回False 因此是要使用or连接
平衡二叉树的返回值是看一下当前根节点的子树高度是否满足小于1再判断它的左右子树是不是小于1 即根节点和左右子树都要满足所以是And来连接三个返回值）
"""
"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构) B是A的子结构，即A中有出现和B相同的结构和节点值。
二叉树的子树和子结构
子树的意思是只要包含了一个结点，就得包含这个结点下的所有节点.
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left = None,right =None):
        self.val = x
        self.left = left
        self.right = right
#         官方题解
class Solution_1:
    # 在A中找B的根节点，如果A的根节点和B的根节点不相等(即A中没有B的子结构)，就递归调用A的左右子树来找B的根节点
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.check(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)

    # 查看子结构是否存在
    def check(self,A:TreeNode, B: TreeNode):
        if not B:
            return True
        # A走到叶子了或者直接就找到一个确切的不等的 说明当前A这颗节点和B不等
        elif not A or A.val != B.val:
            return False
        elif A.val == B.val:
            return self.check(A.left, B.left) and self.check(A.right, B.right)
"""
思路：先在A中找到B的根节点，然后再判断左右子树是不是相等（T.100）
我的思路是错误的，原因是找到了用一个其他函数找开始节点会返回这个孤立的节点，没办法链接下面的左子树和右子树，所以不能把找节点放在一个孤立的函数里
仔细想想，其实差不多，使用isSubStructure()方法在A中找到B的根，思想是看看A的根节点是不是根B相等，不相等的话再看看A的左右子树是不是和B相等，
相当于走一个前序遍历，所以没有要把preorder找根的过程单独找出来，而是直接放在isSubStructure()中即可。
"""
class Solution:
    def preorder(self,A: TreeNode, B: TreeNode):
        # 递归结束条件1
        if not A:
            return None
        # 递归结束条件2
        if A.val == B.val:
            return A
        else:
            return self.preorder(A.left,B) or self.preorder(A.right,B)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        root = self.preorder(A,B)
        return self.check(root,B)

    def check(self,root:TreeNode, B: TreeNode):
        if not root:
            if B:
                return False
        else:
            if not B:
                return True
            elif root.val != B.val:
                return False
            elif root.val == B.val:
                return self.check(root.left, B.left) or self.check(root.right, B.right)

s = Solution()
A = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3))
B = TreeNode(3)
print(s.isSubStructure(A,B))





