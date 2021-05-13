"""一个序列列的⼦子序列列是在该序列列中删去若⼲干元素后得到的序列。
例：“ABCD”和“BDF”都是“ABCDEFG”的子序列
最长公共⼦子序列（LCS）问题：给定两个序列列X和Y，求X和Y⻓长度最⼤大的公共⼦序列。
例例：X="ABBCBDE" Y="DBBCDB" LCS(X,Y)="BBCD"
应⽤场景：字符串串相似度比对

子串：是连续的
子序列：不一定是连续的
"""
def lcs_length(x,y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            # 这里的下标要注意一下，因为二维数组c是从0开始的，但是字符串是从1开始存放的。
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    for _ in c:
        print(_)
    return c[m][n]

def lcs(x,y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 这里的下标要注意一下，因为二维数组c是从0开始的，但是字符串是从1开始存放的。
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                # 左上方箭头
                b[i][j] = 1
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                # 上方箭头
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3
    return c[m][n],b
# 利用回溯法求解动态优化的结果
def lcs_trackback(x,y):
    c,b = lcs(x,y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        # 来自左上方匹配
        if b[i][j] == 1:
            res.append(x[i - 1])
            i -= 1
            j -= 1
        #     来自上方 不匹配
        elif b[i][j] == 2:
            i -= 1
        #     来自左方 不匹配
        else:
            j -= 1
    return "".join(reversed(res))

# BDAB或BCAD都可以
print(lcs_trackback("ABCBDAB","BDCABA"))