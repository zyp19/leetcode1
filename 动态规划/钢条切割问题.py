def cur_rod_recurision_1(p,n):
    if n==0:
        return 0
    else:
        res = p[n]
        for i in range(1,n):
            res = max(res,cur_rod_recurision_1(p,i)+cur_rod_recurision_1(p,n-i))
        return res
# 递归：自顶向下
def cur_rod_recurision_2(p,n):
    if n==0:
        return 0
    else:
        res = 0
        for i in range(1,n+1):
            res = max(res,p[i] + cur_rod_recurision_2(p,n-i))
        return res
# 动态规划：自底向上，把子问题的解存在一个列表中，每次都从列表中去取数
def cut_rod_dp(p,n):
    r = [0]
    for i in range(1,n+1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] +  r[i-j])
        r.append(res)
    return r[n]
# 保留
def cut_rod_extend(p,n):
    r = [0]
    s = [0]
    for i in range(1,n+1):
        # 价格的最优值
        res = 0
        # 价格最大值对应的方案的左边不切割部分的长度
        res_s = 0
        for j in range(1, i + 1):
            # res得到的是最大的r[i]，即最大的长度被保留，如果是长度为5的钢条被切，那么它可以被切成14 23 32 41，而这里shi
            if p[j] +  r[i-j] > res:
                res = p[j] + r[i-j]
                res_s = j
        r.append(res)
        s.append(res_s)
    return r[n],s

def cut_rod_solution(p,n):
    # 通过调用这个函数得到
    r,s = cut_rod_extend(p,n)
    # 存放s[n],即要切割的长度
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans

p = [0,1,5,8,9,10,17,17,20,24,30]
# r,s = cut_rod_extend(p,9)
# print(s)
# print(r)

print(cut_rod_solution(p,10))

