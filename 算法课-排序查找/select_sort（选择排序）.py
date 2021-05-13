# 选择排序：趟数、无序区
def select_sort(list):
    # 趟数
    for i in range(len(list)-1):
        loc = i
        # 无序区
        for j in range(i+1,len(list)):
            if list[loc] > list[j]:
                loc = j
        # 加这一句话的原因是，有可能i就是当前的最小值
        if loc != i:
            list[i],list[loc] = list[loc],list[i]
    return list
result = select_sort([1, 1, 4, 2, 1, 1, 0])
print(result)


