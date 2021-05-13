"""102.二叉树的层次遍历（没有想出来如何返回一个二维数组。。）
这个题的层次遍历的返回值要求返回一个二维的数组（列表），和之前写的返回一维数组不同，因此需要动动脑子。
就像二叉树的求树的结点数目一样巧妙，设置了一个当前值作为加入栈中（在遍历的过程中除了加入结点还加入了这个值表示当前的数目）
这个题也是这样，在遍历队列的时候又设置了一个小循环，循环长度是上个父节点的左右孩子的个数，然后在循环中出队，结束循环后把这个小列表加到大的列表中。。
哎，为什么我就是想不到这个呢？
"""
class Node:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        que = [root]
        if root == None:
            return res
        while que:
            tempList = []
            for i in range(len(que)):
                node = que.pop(0)
                tempList.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tempList)
        return res
solution = Solution()
tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
solution.layerTraverse(tree)


