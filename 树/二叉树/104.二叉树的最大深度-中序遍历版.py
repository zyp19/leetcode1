class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Node):
        # 当前深度
        curdepth = 0
        # 最大深度
        depth = 0
        stack = []
        r = root
        while r or stack:
            # depth = max(depth,curdepth)
            while r:
                curdepth += 1
                stack.append((curdepth, r))
                r = r.left
            if stack:
                curdepth ,r = stack.pop(-1)
                r = r.right
            depth = max(depth, curdepth)
        return depth

solution = Solution()
tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
# tree = Node(1, None,Node(2))
result = solution.maxDepth(tree)
print(result)