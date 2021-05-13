# 找零问题
# Date: 2018/4/14
# t是倒序排的
t = [100, 50, 20, 5]

def change(t, n):
    # m是初始化len(t)，“_”是一个循环标志，可以用i,j等字母代替，下面的循环不会用到，即是一个只存在于本循环的变量，起到的是循环此数的作用
    # m =[0,0,0,0]
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n

print(change(t, 376))