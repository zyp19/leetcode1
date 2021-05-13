"""617.合并二叉树（双树 无辅助函数 先序/后序遍历 改变树（给树的节点赋值） 所以要把返回值付给节点）
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为NULL 的节点将直接作为新二叉树
的节点。
注意: 合并必须从两个树的根节点开始。
"""
"""
双树+先序遍历
且是调整整棵树的题目，最后返回根节点，那么调用左右子树的函数的时候一定是返回左子树和右子树，因为要给左右子树赋值，所以一定要有返回值才行
相似的题还有226，但是226虽然也是需要调整一棵树，但是其关键在于交换子树，所以不存在给左右子树赋值的问题，所以就先序遍历不用返回值。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
注意这种做法是错误的，我这样做的初衷是想要改变树，但是root1为空的情况下，第25行是不成立的，所以说会报错
"""
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 这里可以精简一下前面的判断条件
        if not root1:
            root1 = root2
        if not root2:
            root1 = root1
        # if not root1 and not root2:
        #     return root1
        # if not root1 and root2:
        #     return  root2
        # elif not root2 and root1:
        #     return  root1
        elif root1 and root2:
            root1.val = root1.val + root2.val
        self.mergeTrees(root1.left,root2.left)
        self.mergeTrees(root1.right,root2.right)
        return root1
"""
正确做法：先给根节点赋值（递归前面的部分），再给左右子树赋值（左右子树先序遍历）！
"""
class Solution1:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        if root1 and root2:
            root1.val = root1.val + root2.val
            # return root1 #思考：这一句话为什么不加？傻了吧？加了这一句符合if的时候不就直接返回了吗。。。就不会执行下面的递归了
        root1.left = self.mergeTrees(root1.left,root2.left)
        root1.right = self.mergeTrees(root1.right,root2.right)
        return root1

s = Solution1()
t1 = TreeNode(1,TreeNode(3,TreeNode(5)),TreeNode(2))
t2 = TreeNode(2,TreeNode(1,None,TreeNode(4)),TreeNode(3,None,TreeNode(7)))
s.mergeTrees(t1,t2)