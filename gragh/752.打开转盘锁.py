"""752.打开转盘锁
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转:
例如把 '9' 变为'0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。"""
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusone(s: str, j: int) -> str:
            ch = list(s)
            if ch[j] == '9':
                ch[j] = '0'
            else:
                ch[j] = str(int(ch[j]) + 1)
            return "".join(ch)
        def minusone(s: str, j: int) -> str:
            ch = list(s)
            if ch[j] == '0':
                ch[j] = '9'
            else:
                ch[j] = str(int(ch[j]) - 1)
            return "".join(ch)
        deads = set(deadends)
        visited = set()
        queue = []
        step = 0
        queue.append("0000")
        visited.add("0000")
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur in deads:
                    continue
                if cur == target:
                    return step
                for j in range(4):
                    up = plusone(cur, j)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    down = minusone(cur, j)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            step += 1
        return -1
# s = Solution()
# print(s.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
# 双向bfs
class Solution_1:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        q1,q2 = set(),set()
        q1.add("0000")
        q2.add(target)
        visited = set()
        step = 0
        #向四周扩散
        while q1 and q2 :
            temp = set()
            # 采用较小的集合进行扩散
            if (len(q1) > len(q2)):
                q1,q2 = q2,q1
            # 遍历q1的中的节点
            for cur in q1:
                if cur in dead:
                    continue
                #   q1 q2产生交集
                if cur in q2:
                    return step
                visited.add(cur)
                #将节点的相邻节点加入队列
                for i in range(4):
                    up_str = self.upString(cur,i)
                    down_str = self.downString(cur,i)
                    if up_str not in visited:
                        # 注意65行遍历了q1集合，所以这里不能在循环里修改其q1集合，要使用temp
                        temp.add(up_str)
                    if down_str not in visited:
                        temp.add(down_str)
            step += 1
            q1 = q2
            q2 = temp
        return -1
    # 将s[i]向上拨动一次
    def upString(self, s: str, i: int) -> str:
        ls = list(s)
        if ls[i] == "9":
            ls[i] = "0"
        else:
            ls[i] = str(int(ls[i]) + 1)
        return "".join(ls)

    # 将s[i]向下拨动一次
    def downString(self, s: str, i: int) -> str:
        ls = list(s)
        if ls[i] == "0":
            ls[i] = "9"
        else:
            ls[i] = str(int(ls[i]) - 1)
        return "".join(ls)
s = Solution_1()
print(s.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))