"""652.寻找重复的子树
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。两棵树重复是指它们具有相同的结构以及相同的结点值。
"""
from typing import List
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
思路：把每一颗子树都放到字典中，如果字典中该子树的个数超过两个就返回根节点；而描述二叉树的结构可以用到“二叉树的序列化和反序列化”
"""
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        counter = Counter()
        return self.dfs(root,counter)
    def dfs(self,root,counter):
        if not root:
            return "#"
        # 放根节点的列表
        res = []
        l = self.dfs(root.left,counter)
        r = self.dfs(root.right,counter)
        yes = l + "," + r + "," + str(root.val)
        counter[yes] += 1
        if counter[yes] == 2:
            # 不可以把res作为局部变量使用，原因是dfs这个函数的返回值是yes（即树结构序列化之后的结果），res中存的是根节点，如果函数返回的是res就可以了
            res.append(root)
        return yes
