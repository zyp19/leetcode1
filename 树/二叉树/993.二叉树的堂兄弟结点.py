"""993. 二叉树的堂兄弟节点
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
"""
"""
思路：1.求给定结点的深度 2.把父节点，深度，该结点三个都入栈！5.19ac
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root, x: int, y: int):
        if root is None:
            return 0
        stack = [(1, 0, root)]
        result = []
        while stack:
            cur_dep, parent_val, node = stack.pop()
            if node.val == x or node.val ==y:
                result.append([cur_dep, parent_val, node])
            if node.right:
                stack.append((cur_dep+1,node.val,node.right))
            if node.left:
                stack.append((cur_dep+1,node.val,node.left))
        if result[0][0] == result[1][0] and result[0][1] != result[1][1]:
            return True
        else:
            return False
solution = Solution()
tree = Node(1, Node(2, Node(4)), Node(3))
re = solution.isCousins(tree,4,3)
print(re)



