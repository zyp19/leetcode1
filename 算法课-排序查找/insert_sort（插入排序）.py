"""
4.20看，5.6不记得了
"""
def insert_sort(list):
    # 摸到的牌
    for i in range(1,len(list)):
        # 摸到的牌（无序区）
        temp = list[i]
        # 手里的牌（有序区）
        j = i-1
        # 想不明白为什么这里是list[j] > temp而不是>list[i]
        # 想清楚了：因为做有序区的后移操作的时候，面临着一个赋值操作，这时候有可能把list[i]被list[j]覆盖，所以list[i]不是一个固定的值
        while j >= 0 and list[j] > temp:
            list[j + 1] = list[j]
            j -= 1
        list[j+1] = temp
    return list
result = insert_sort([2,3,1,7,4,6,5])
print(result)


