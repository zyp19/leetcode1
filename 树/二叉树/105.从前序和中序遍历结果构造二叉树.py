"""105.从前序和中序遍历结果构造二叉树
注意:
你可以假设树中没有重复的元素。
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
思路：我的想法是从前序遍历中找到根节点，从中序遍历中找到左右子树，想法很好，但是不知道如何通过有限的参数找到根节点，所以选择看题解
"""
# 讨厌指针 喜欢切片
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        return self.findRootIndex(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
    # 构造树，指针的做法好乱，官方题解说用切片的方法做好
    def findRootIndex(self,preorder, preS, preE, inorder, inS, inE):
        if preS > preE:
            return None
        root = TreeNode()
        # 不知道如何通过有限的参数找到根节点
        # 根节点肯定是起始数组的第一个元素，
        root.val = preorder[preS]
        # 找到根节点在中序遍历的位置
        rootIndex = preS
        for i in range(inS,inE):
            if inorder[i] == root.val:
                rootIndex = i
                break
        # 左子树长度
        len_L = rootIndex - inS
        #  实际上是一个绝对位置，绝对长度
        root.left = self.findRootIndex(preorder, preS+1, preS + len_L, inorder, inS, rootIndex-1)
        root.right = self.findRootIndex(preorder, preS + len_L+1, preE, inorder, rootIndex + 1, inE)
        return root
s = Solution()
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
s.buildTree(preorder,inorder)
#     切片的方法
class Solution_1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 这里判断用中序和前序都可以
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        # 根据值查找下标
        idx = inorder.index(root.val)
        # 妙啊！根节点在中序遍历的下标其实同时也是左子树的个数，算是一个相对位置（相对于开始的位置）
        root.left = self.buildTree(preorder[1: idx + 1], inorder[0: idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1: ])
        return root

# 加入哈希，降低查找的时间复杂度
class Solution_2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归+前序遍历，哈希映射降低时间复杂度
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        def tree(root, left, right):
            if left > right:
                return
            node = TreeNode(preorder[root])
            k = dic[preorder[root]]
            # 这个不是左开右闭
            node.left = tree(root+1, left, k-1)
            node.right = tree(root+k-left+1, k+1, right)
            return node
        node = tree(0, 0, len(preorder)-1)
        return node