# 第一题：幸运员工抽奖
# 题目描述：
# 从团队中选出整个工号中含有数字7或者工号是7的倍数的员工。
# 输入：一组空格分隔的员工工号列表。
# 输出：幸运员工总人数，未找到时输出0。

# 输入是数字，该数字中包含7或它是7的倍数的返回正确，并且输出的是员工的人数
m = list(map(int,input().split(" ")))
def check(m):
    n = 0
    for num in m:
        if num % 7 == 0:
            n += 1
            continue
        # 数字转字符串
        else:
            s = str(num)
            if '7' in s:
                n += 1
                continue
    print(n)
check(m)

