"""652.寻找重复的子树
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
两棵树重复是指它们具有相同的结构以及相同的结点值。
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
思路：把每一颗子树都放到字典中，如果字典中该子树的个数超过两个就返回根节点；而描述二叉树的结构可以用到“二叉树的序列化和反序列化”
"""
# 后序遍历
import collections
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """序列化整颗树的子树序列, 如果已存在这样的子树, 则输出
        """
        res = []
        counter = collections.Counter()

        def traverse(root):
            if not root: return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            chain = left + ',' + right + ',' + str(root.val)
            counter[chain] += 1
            if counter[chain] == 2:
                res.append(root)
            return chain

        traverse(root)
        return res
s = Solution()
t1 = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3,TreeNode(2,TreeNode(4)),TreeNode(4)))
print(s.findDuplicateSubtrees(t1))
# 后序遍历
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ans, d = [], {}
        def f(r):
            if not r:
                return 'N'
            # 每次递归都会更新该式子，所以实际上是后序遍历
            s = str(r.val) + ' ' + f(r.left) + ' ' + f(r.right)
            if s not in d:
                # 如果不在，就加进去并把值设为true
                d[s] = True
            elif d[s]:
                # 如果在，就把根节点加到ans中，并把值设为false（为了下一次再得到重复子树的时候防止会产生再把根节点加进去的情况，也就是重复子树的根节点只出现一次即可，这也是为什么
                # 如果设置出现次数而不是布尔值的时候采用的是出现次数为2的时候才加到字典中）
                ans.append(r)
                d[s] = False
            return s
        f(root)
        return ans
# 后序遍历
class Solution_1:
    # 全局变量的使用
    def __init__(self):
        self.dict = {}
        self.arr = []
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.postorder(root)
        return self.arr
    # 计算每一个二叉树的结构（使用二叉树的序列化），并放到字典中；并对每一个结点都做序列化放到字典中
    def postorder(self,root):
        if not root:
            return "None"
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        # 每次递归这一句都会被重新赋值，也就是每个根节点及它的子树会有一个这个值
        yas = left + ','+right + ','+str(root.val)
        # 字典的定义
        self.dict[yas] = self.dict.setdefault(yas,0)+1
        if self.dict[yas] == 2:
            self.arr.append(root)
        return yas
s = Solution_1()
t1 = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3,TreeNode(2,TreeNode(4)),TreeNode(4)))
print(s.findDuplicateSubtrees(t1))

# 先序遍历，死慢，因为有重复子问题
class Solution_2:
    # 凡是每次递归涉及到一个全局值改变的，都要在init函数中进行全局值的设置，避免在递归函数中设置局部值
    def __init__(self):
        self.dict = {}
        self.res = []
    # 每个子树都要调用该二叉树序列化函数，输入根节点及其子树，得到该根节点值和子树的值（皆为字符串）
    def serialize(self,root:TreeNode):
        if not root:
            return "None"
        # 这里注意一下是需要的到字符串，所以需要把int类型的val值转变为str类型的
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return None
        # 调用只能调用别人的根节点 不能在这里传左右子树，原因是不能递归调用，因为递归是自己调用自己
        self.times(root)
        return self.res
    def times(self,root):
        if not root:
            return
        # 因为这里times输入结点，每一次都对该节点及其子树进行序列化，因此这里是把每颗树的序列化结果算了出来
        yas = self.serialize(root)
        # 把每个yas加入到字典dict中
        self.dict[yas] = self.dict.get(yas,0)+1
        if self.dict[yas] == 2:
            self.res.append(root)
        self.times(root.left)
        self.times(root.right)
s = Solution_2()
t1 = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3,TreeNode(2,TreeNode(4)),TreeNode(4)))
print(s.findDuplicateSubtrees(t1))
# 先序遍历
from collections import Counter
class Solution_3:

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """序列化整颗树的子树序列, 如果已存在这样的子树, 则输出
        """
        def serialize(root):
            if not root:
                return '#'
            return str(root.val) + ',' + serialize(root.left) + ',' + serialize(root.right)
        # 不在init中设置全局的坏处导致了需要传参字典counter和res每次都需要置空
        def traverse(root, counter) -> List['TreeNode']:
            if not root:
                return []
            res = []
            chain = serialize(root)
            counter[chain] += 1
            if counter[chain] == 2:
                res.append(root)
            #     我真的不能理解为什么这里的res是局部变量每次都置零，还能最终出来结果，好像明白了，res在每次递归栈中都存一份值，左右子树若使res这个列表有值
            # 那么就会返回调用它的根节点，这个时候就能达到相加的作用，真的是妙啊！！！
            res += traverse(root.left, counter) + traverse(root.right, counter)
            return res
        return traverse(root, Counter())
s = Solution_3()
t1 = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3,TreeNode(2,TreeNode(4)),TreeNode(4)))
print(s.findDuplicateSubtrees(t1))
