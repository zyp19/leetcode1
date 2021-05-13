"""589. N 叉树的前序遍历
给定一个 N 叉树，返回其节点值的 前序遍历 。
N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""
# Definition for a Node.
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return []
        res.append(root.val)
        for i in root.children:
            res += self.preorder(i)
        return res
