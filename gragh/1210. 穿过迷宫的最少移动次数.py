"""1210. 穿过迷宫的最少移动次数
"""
from typing import List
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        visited = set("0001")
        n = len(grid)
        step = 0
        target = str(n-1)+str(n-2)+str(n-1)+str(n-1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid = ""+str(grid[i][j])
        q = []
        q.append("0001")
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur == target:
                    return step
                cur = list(cur)
                # 如果右边没有障碍
                if str(int((cur[-1])+1)=="0":
                    cur="".join(cur)
                    q.append(cur[2:]+cur[0]+"0")
                if str(int(cur[-2]+n-1))=="0"

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        start = (0, 0, 0, 1)
        end = (n - 1, n - 2, n - 1, n - 1)
        if grid[0][0] == 1 or grid[0][1] == 1 or grid[n - 1][n - 2] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        Q = collections.deque()
        visited = set()
        Q.append(start)
        visited.add(start)
        step = 0
        while Q:
            cur_len = len(Q)
            for _ in range(cur_len):
                r1, c1, r2, c2 = Q.popleft()
                if (r1, c1, r2, c2) == end:
                    return step
                # ------------------------------------ 蛇身水平
                if r1 == r2:
                    # ------------- 右侧是空的，往右走一步
                    if c2 + 1 < n and grid[r2][c2 + 1] != 1 and (r2, c2, r2, c2 + 1) not in visited:
                        Q.append((r2, c2, r2, c2 + 1))
                        visited.add((r2, c2, r2, c2 + 1))
                        # ------------- 下侧都是空的
                    if r1 + 1 < n and grid[r1 + 1][c1] != 1 and grid[r1 + 1][c2] != 1:
                        # ---- 下移
                        if (r1 + 1, c1, r2 + 1, c2) not in visited:
                            Q.append((r1 + 1, c1, r2 + 1, c2))
                            visited.add((r1 + 1, c1, r2 + 1, c2))
                        # ---- 顺时针
                        if (r1, c1, r1 + 1, c1) not in visited:
                            Q.append((r1, c1, r1 + 1, c1))
                            visited.add((r1, c1, r1 + 1, c1))
                # ------------------------------------ 蛇身竖直
                if c1 == c2:
                    # ------------- 下侧是空的，往下一步
                    if r2 + 1 < n and grid[r2 + 1][c2] != 1 and (r2, c2, r2 + 1, c2) not in visited:
                        Q.append((r2, c2, r2 + 1, c2))
                        visited.add((r2, c2, r2 + 1, c2))
                    # ------------ 右侧2点都是空的
                    if c1 + 1 < n and grid[r1][c1 + 1] != 1 and grid[r2][c2 + 1] != 1:
                        # ---- 右移
                        if (r1, c1 + 1, r2, c2 + 1) not in visited:
                            Q.append((r1, c1 + 1, r2, c2 + 1))
                            visited.add((r1, c1 + 1, r2, c2 + 1))
                        # ---- 逆时针
                        if (r1, c1, r1, c1 + 1) not in visited:
                            Q.append((r1, c1, r1, c1 + 1))
                            visited.add((r1, c1, r1, c1 + 1))
            step += 1
        return -1