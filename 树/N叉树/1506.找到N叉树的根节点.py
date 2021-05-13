"""1506.找到n叉树的根节点
给定一棵 N 叉树 的所有节点在一个数组  Node[] tree 中，树中每个节点都有 唯一的值 。
找到并返回 N 叉树的 根节点 。
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# map存子->父
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children_vals = set()

        for node in tree:
            for child in node.children:
                children_vals.add(child.val)

        for node in tree:
            if node.val not in children_vals:
                return node