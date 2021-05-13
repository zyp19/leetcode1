"""297.二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机
环境，采取相反方式重构得到原数据。请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个
二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
"""
"""
题目理解：二叉树的序列化就是指把二叉树序列化一个字符串；二叉树的反序列化就是将字符串再化为原始的树结构
所谓的序列化不过就是把结构化的数据「打平」，其实就是在考察二叉树的遍历方式。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    # 序列化很简单，写一个前序遍历输出结点，注意输出#和最后一位是","（不要输出）
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # 字符串是不能改变的，所以这里应该定义一个List（错误！字符串不可改变是可以覆盖原字符串，但是不能逐位去修改，但是可以使用字符串拼接操作给字符串增添内容，
        # 而且需要返回str,不能定义List）
        # 复习：列表转字符串
        # 方法1
        # >> > list1 = ['ak', 'uk', 4]
        # >> > list2 = [str(i) for i in list1]  # 使用列表推导式把列表中的单个元素全部转化为str类型
        # 方法2
        # list2 = ['hello', 'world']
        # # 引号中的内容为，连接各个字符串的字符
        # print("".join(list2))
        # print(" ".join(list2))
        # print(".".join(list2))
        # 输出：helloworld
        # 输出：hello world
        # 输出：hello.world
        # 字符串转列表
        # str3 = "en oo nn"
        # list3 = str3.split() -->['en','oo','nn']
        # list2 = str3.split(" ")-->['en','oo','nn']
        # 字符串的拼接操作，由于字符串是不可修改的，如果想给字符串中增添内容，可以使用字符串拼接操作，即相同字符类型用逗号拼接，不同字符类型用加号拼接
        str = ""
        if not root:
            return "#"
        # 序列化结果为前序遍历
        return str(root.val)+","+str(self.serialize(root.left))+","+str(self.serialize(root.right))

    """ 先将字符串转化成列表，使用：data = "1,2,#,4,#,#,3,#,#,"  arr = data.split(",")
    列表就是二叉树的前序遍历结果，问题转化为：如何通过二叉树的前序遍历结果还原一棵二叉树？
    PS：一般语境下，单单前序遍历结果是不能还原二叉树结构的，因为缺少空指针的信息，至少要得到前、中、后序遍历中的两种才能还原二叉树。
    但是这里的列表包含空指针的信息，所以只使用列表就可以还原二叉树。根据我们刚才的分析，列表就是一棵打平的二叉树："""
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # 将字符串转成列表
        arr = data.split(",")
        return self.preorder(arr)

    def preorder(self, arr):
        val = arr.pop(0)
        if val == "None":
            return None
        root = TreeNode(int(val))
        root.left = self.deserialize(arr)
        root.right = self.deserialize(arr)
        return root
