"""1522.N叉树的直径
给定一棵 N 叉树的根节点root，计算这棵树的直径长度。
N 叉树的直径指的是树中任意两个节点间路径中 最长 路径的长度。这条路径可能经过根节点，也可能不经过根节点。
N 叉树的输入序列以层序遍历的形式给出，每组子节点用 null 分隔）
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
class Solution_1:
    def __init__(self):
        self.height = 0
    def diameter(self, root: 'Node') -> int:
        self.sumHeight(root)
        return self.height
    def sumHeight(self,root):
        if not root:
            return 0
        h = 0
        res = []
        for node in root.children:
            c_l = self.sumHeight(node)
            h = max(h,c_l)
            res.append(c_l)
        res.sort(reverse = True)
        self.height = max(self.height,sum(res[:2]))
        return h + 1
s = Solution_1()
t = Node(1,[Node(3,[Node(5),Node(6)]),Node(2),Node(4)])
print(s.diameter(t))

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.res = 0
        def dfs(root):
            dep = [0, 0]
            if root:
                for ch in root.children:
                    dep.append(dfs(ch))
                dep.sort(reverse = True)
            self.res = max(self.res, sum(dep[:2]))
            return dep[0] + 1
        dfs(root)
        return self.res
# s = Solution()
# t = Node(1,[Node(3,[Node(5),Node(6)]),Node(2),Node(4)])
# print(s.diameter(t))