"""114.二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
"""
"""
思路：后序遍历：有左子树时，把左子树插入到根和右子树之间（tmp = root.right, root.right = root.left, root.left.right = tmp）

"""
class Solution:
    # 方法1，使用后序遍历构造链表
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        # 5.30第一次做 发现后序遍历的模板有一个很有用的规律，可以记住：
        # 先走左子树 再走21行之后的操作 之后右子树再走21行的操作 这就是后序遍历的精髓！！
        # 即不用管左子树走的过程中右子树的操作，因为都是走的15-16行，所以都是返回None值
        self.flatten(root.left)
        self.flatten(root.right)
        # 6.12复习备注注意：此时左右结点已经按照下面的定义完成相应的链表展平，所以下面的定义就以根节点所作的事为准，左右子树按照此定义做即可，所以这里不能
        # 出现与上面左右子树相关的任何东西（如果获取左右子树的返回值的话，因为获取左右子树的返回值往往是要进行判断的，比如平衡二叉树拿到图），只需要根节点的操作定义每个结点的操作即可
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right= tmp
    # 6.12方法2：使用先序遍历构造,我的天，道理居然和方法一一样！！！但是这样做不对噢！会失去一部分的左右节点的引用！
    # 6.18再次复习：为什么同样都是插入左节点到根节点和右节点之间，后序遍历就不会失去右指针，先序遍历就会失去呢？原因在于后序遍历是先进行递归，在递归栈中已经
    # 存储了root.right和root.left的地址，如21 22行所示，但是先序遍历是进行了根节点左右指针的变换，所以再进行43和44的递归时已经失去了root的左右孩子的地址了！
    def createList(self,root):
        if not root:
            return None
        tmp = root.right
        root.right = root.left
        # 把右子树挂在左子树的最后孩子的右子树上
        while root.right:
            root = root.right
        root.right =tmp
        self.createList(root.left)
        self.createList(root.right)
    # 6.12 方法2：使用先序遍历按照题解的做法重新做
    def flatten(self, root) -> None:
        if not root:
            return None
        res = self.dfs(root)
        # 思路是把二叉树的所有节点都放在一个列表List中，然后通过在其中取节点构造链表即可，构造链表就是要有一个pre，一个cur
        for i in range(1,len(res)):
            pre,cur = res[i-1],res[i]
            pre.left = None
            pre.right = cur
    def dfs(self,root):
        if not root:
            return None
        return [root]+self.dfs(root.left)+self.dfs(root.right)
