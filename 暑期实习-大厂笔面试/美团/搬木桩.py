"""搬m个木桩，高度最大是h，大于h的就搬不过去。
题目描述：
小美和小团要搬家,他们要把家具从围栏上搬过去.围栏由n个独立的木桩排成一条直线组成,第i个木桩编号为i.由于他们体力的限制,只能越过高度不高于h的围栏,
同时家具又要有宽度限制,只有连续m个木桩都能搬过去才能成功将家具搬过去.现在他们想知道他们能否成功搬家.
输入描述
第一行三个整数n,m和h，含义如上文所述。
第二行n个整数，height1,...,heightn，依次表示每个木桩的高度。
1≤m≤n≤105,0≤h,heighti≤109。
输出描述
输出一个整数，若能成功搬家,输出第一个跨过的木桩的编号,若有多组答案输出最小的。否则,输出整数-1。
样例输入
5 3 2
3 2 1 1 2
样例输出
2
"""
def function(n, m, h, num):
    l,r = 0,0
    t = 0
    while r < n:
        flag = l
        i = 0
        while i < m and r<n:
            if num[r] > h:
                i = 0
                r,l = r+1,r+1
                flag = l
            else:
                r += 1
                i = r - l + 1
        if flag > l:
            flag = l
        t = i
    if t < m:
        return -1
    return flag +1

result = function(4,3,2,[3,4,5,4])
print(result)
# while True:
#     # 长度 必须搬的木桩的个数 高度
#     n,m,h = map(int, input().split())
#     # 树桩的具体内容
#     num = [int(i) for i in input().split(" ")]
