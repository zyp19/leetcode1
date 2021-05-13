# 动态规划的思想-最优子结构（递推式），在斐波那契数列中，递推式已经规定好了。
# 特点：子问题已经计算好了，存到一个列表中，然后计算下面的问题时，会从列表中取
def fibnacci_no_recurision(n):
    f = [0,1,1]
    # 从n=3开始
    if n>2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]
print(fibnacci_no_recurision(100))

def fibanacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibanacci(n-1) + fibanacci(n-2)
# f(5) = f(4)+f(3)
# f(4) = f(3)+f(2)
# f(3) = f(2)+f(1)
# f(3) = f(2)+f(1)
# f(2) = 1
# 递归的写法是含有子问题的重复计算