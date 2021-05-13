class Solution:
    def slidingPuzzle(self, board) -> int:
        # 将二维数组压缩成字符串
        start = ""
        target = "123450"
        for i in range(2):
            for j in range(3):
                start = start+str(board[i][j])
        print(start)
        neighbor = ((1,3),(0,4,2),(1,5),(0,4),(3,1,5),(4,2))
        step = 0
        q = []
        q.append(start)
        visited = set(start)
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur==target:
                    return step
                m = cur.index("0")
                for j in neighbor[m]:
                    new_board = list(cur)
                    new_board[m],new_board[j] = new_board[j],new_board[m]
                    new_board = "".join(new_board)
                    if new_board not in visited:
                        q.append(new_board)
                        visited.add(new_board)
            step += 1
        return -1
s = Solution()
print(s.slidingPuzzle(board = [[1,2,3],[4,0,5]]))