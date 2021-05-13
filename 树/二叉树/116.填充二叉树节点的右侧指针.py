"""116.填充二叉树节点的右侧指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有next 指针都被设置为 NULL。

题目的意思就是把二叉树的每一层节点都用 next 指针连接起来：而且题目说了，输入是一棵「完美二叉树」，形象地说整棵二叉树是一个正三角形，
除了最右侧的节点 next 指针会指向 null，其他节点的右侧一定有相邻的节点。
"""
"""
二叉树题目的一个难点就是，如何把题目的要求细化成每个节点需要做的事情。
写树相关的算法，简单说就是，先搞清楚当前 root 节点该做什么，然后根据函数定义递归调用子节点，递归调用会让孩子节点做相同的事情。
写递归算法的关键是要明确函数的「定义」是什么，然后相信这个定义，利用这个定义推导最终结果，绝不要跳入递归的细节。
root.left.next = root.right
root.right.next = root.right
这种一个root节点传参是做不到的，那么一个节点做不到，就使用两个节点
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # 只连接左右子树，发现并不能把5 6节点连接起来，因此要使用两个节点
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        left = self.connect(root.left)
        right = self.connect(root.right)
        self.twonode_connect(left,right)
        # right.next = None
        # root.next = None
        return root


    def twonode_connect(self,node1,node2):
        if node1 and node2:
            node1.next = node2
        if not node1 and not node2:
            return None
        self.twonode_connect(node1.left,node1.right)
        self.twonode_connect(node1.right,node2.left)
        self.twonode_connect(node2.left,node2.right)

