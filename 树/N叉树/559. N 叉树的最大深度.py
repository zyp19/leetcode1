"""559. N 叉树的最大深度
给定一个 N 叉树，找到其最大深度。
最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def height(root):
            if not root:
                return 0
            h = 0
            # 关于h是局部变脸的问题，每次递归调用时，每个函数栈里都会生成一个h变量，但是函数返回到调用其处，进行比较的h实际是上一层栈中的变量。
            # 划重点：注意写的时候h要写在for循环的外面！
            for node in root.children:
                if h < height(node):
                    h = height(node)
            return h+1
        return height(root)

class Solution_2:
    def __init__(self):
        self.h = 0
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        for node in root.children:
            self.h = max(self.h,self.maxDepth(node))
        return self.h+1
