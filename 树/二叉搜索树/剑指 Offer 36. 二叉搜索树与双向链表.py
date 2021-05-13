"""剑指 Offer 36. 二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
为了让您更好地理解问题，以下面的二叉搜索树为例：
我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个
节点的后继是第一个节点。
下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 1.知道应该是先构造树中结点的连接，但是不知道怎么构造头结点和尾结点与其他结点的连接；2.没有读清题意，应是left代表前驱，right代表后继。
# 3.该题使用中序遍历，但是我并没有弄明白中序遍历的输出地应该是些什么：应该写的是当前节点该做的事情，而不是像滴26行那样写成left需要做什么，属于概念模糊不清。
# 这就是所说的框架问题，需要将问题细化到每个结点应该做什么事情上。
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        h = self.createList(root)
    def createList(self,root:'Node'):
        if not root:
            return None
        left = self.treeToDoublyList(root.left)
        h = left.right
        if h:
            # h为最右的结点
            while h.right:
                h = h.right
            root.prior = h
            h.next = root
        else:
            left.next = root
        right = self.treeToDoublyList(root.right)
        right.prior = root
        return root
# 看了题解，意识到自己的问题后，尝试修改一下：
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        h = self.createList(root)
    def createList(self,root:'Node'):
        if not root:
            return None
        l = self.treeToDoublyList(root.left)
        r = self.treeToDoublyList(root.right)
        h = l.right
        # root的左子树的右孩子存在
        if h:
            # h为最右的结点
            while h.right:
                h = h.right
            root.left = h
            h.right = root
        # root的左子树的右孩子不存在
        else:
            l.right = root
        root.left = r
        return root
# 正儿八经看了题解
class Solution:
    def __init__(self):
        self.pre = None
        self.head, self.tail = None,None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.treeToDoublyList(root.left)
        if not self.pre:
            # 构建头尾结点
            self.head = root
            self.head.right = self.tail
            self.tail.left = self.head
        else:
            # 构建中间结点
            self.pre.right = root
            root.left = self.pre
            root.right = self.tail
        self.pre = root
        self.treeToDoublyList(root.right)
        return self.head
# 第二遍看题解
class Solution:
    def __init__(self):
        self.pre = None
        # self.head, self.tail = None,None
        # self.head = None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.inorder(root)
        # 原则是指针指向结点，但是这里head意为结点
        self.head.left = self.pre
        self.pre.right = self.head
    def inorder(self,root):
        if not root:
            return None
        self.inorder(root.left)
        if not self.pre:
            # 构建头尾结点
            self.head = root
            # self.head.right = self.tail
            # self.tail.left = self.head
        else:
            # 构建中间结点
            self.pre.right = root
            root.left = self.pre
            # root.right = self.tail
        self.pre = root
        self.inorder(root.right)
        return self.head

class Solution:
    def __init__(self):
        self.pre = None
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.inorder(root)
        # 原则是指针指向结点，但是这里head指代它指向的结点，所以是节点
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
    def inorder(self,root):
        if not root:
            return None
        self.inorder(root.left)
        if not self.pre:
            # 构建头尾结点
            self.head = root
        else:
            # 构建中间结点
            self.pre.right = root
            root.left = self.pre
        self.pre = root
        self.inorder(root.right)
        return self.head



