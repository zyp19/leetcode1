from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # inorder和postorder的长度一致，所以判断哪个都行
        if not postorder:
            return None
        node = TreeNode(postorder[-1])
        idx = inorder.index(node.val)
        node.left = self.buildTree(inorder[:idx], postorder[:idx])
        node.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return node