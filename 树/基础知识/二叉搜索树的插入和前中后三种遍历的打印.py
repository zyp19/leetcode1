class BiTreeNode(object):
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None
class BST:
    def __init__(self,li = None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)
    def pre_order(self,root):
        if root:
            # end参数的含义是关闭自动换行
            print(root.data,end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
    def in_order(self,root):
        if root:
            # end参数的含义是关闭自动换行
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)
    def post_order(self,root):
        if root:
            # end参数的含义是关闭自动换行
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
            print(root.data,end=',')
    # 非递归的节点插入
    def insert_no_rec(self,val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            # 没有根节点的情况
            return
        # 插入的节点是一定在叶子节点中的
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                # 走了这一个else分支说明找到了查找的位置，说明需要执行插入操作；
                # 插入的节点一定是在叶子节点
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                # 走了这一个else分支说明找到了查找的位置，说明需要执行插入操作；
                # 插入的节点一定是在叶子节点
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            # 如果是val和遍历到的某节点的值相同的情况，那就什么都不做，直接return。就如同集合操作，重复的节点不进入集合中。
            else:
                return
tree = BST([4,6,1,9,2,1,3,8])
tree.pre_order(tree.root)
print("")
# 发现中序排序的二叉搜索树是一个有序树，因为按照二叉搜索树的定义和中序排序能够符合上。
tree.in_order(tree.root)
print("")
tree.post_order(tree.root)

