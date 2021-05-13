"""513.找左下角的值
给定一个二叉树，在树的最后一行找到最左边的值。
"""
"""
思路：找到层数最高的叶子结点的值即可
"""
# 局部变量的使用1：通过传递参数的方法来实现局部变量的修改
class Solution:
    def __init__(self):
        self.h = 0
        self.val = 0
    def findBottomLeftValue(self, root) -> int:
        self.level(root,level=1)
        return self.val
    # 通过传递参数的方法来实现局部变量的修改
    def level(self,root,level):
        if level > self.h:
            self.h = level
            self.val = root.val
        self.level(root.left,level + 1)
        self.level(root.right, level + 1)
# 局部变量的使用2：通过递归函数的返回值获取变量值的方法来实现局部变量的修改,这种是不可取的，原因是会从被调用者往调用者返回，所以是从叶子结点往根节点返回，
# 因此是从根节点处的值最大。这种方法可以用来求根节点的高度
class Solution_1:
    def __init__(self):
        self.h = 0
        self.val = 0
    def findBottomLeftValue(self, root) -> int:
        self.level(root)
        return self.val
    def level(self,root):
        if not root:
            return
        l = 0
        l += 1
        if l > self.h:
            self.h = l
            self.val = root.val
        self.level(root.left)
        self.level(root.right)
        return l