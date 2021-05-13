"""124.二叉树中的最大路径和
给定一个非空二叉树,任意选择两个节点(可以是同一个节点),两个节点必然可以通过唯一的一个路径连接,计算该路径上所有节点(包括这两个节点)的val值和.
返回其中的最大值.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""思路：
左子树权值和右子树权值比较，选择一个大的和根节点权值相加（如果使根结点权值变小就不要相加），作为这一个根节点代表着的子树的权值（相当于求二叉树
的最大权值结点）
设置叶子结点一开始的值为self.max，如果加上该根节点变小了就不要相加，但是根节点代表的子树的权值还是要计算出来，因为有可能下一步会有大的值
"""
class Solution:
    def __init__(self):
        self.max = float('-inf')
    def maxPathSum(self, root: TreeNode)-> int:
        self.rootPathSum(root)
        return self.max
    # 求每个结点代表的子树的权值
    def rootPathSum(self,root: TreeNode):
        if not root:
            return 0
        l = self.rootPathSum(root.left)
        r = self.rootPathSum(root.right)
        # 用于剪枝，原因是，如果算得的这一分支是负值，那么就没必要把它给加进来，就剪枝
        if l < 0:
            l = 0
        if r < 0:
            r = 0
        sum = root.val
        if max(l,r) + root.val > sum:
            sum += max(l,r)
        if l + r + root.val > self.max:
            self.max = l + r + root.val
        return sum
s = Solution()
t1 = TreeNode(-10,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
t2 = TreeNode(2,TreeNode(-1))
print(s.maxPathSum(t2))

