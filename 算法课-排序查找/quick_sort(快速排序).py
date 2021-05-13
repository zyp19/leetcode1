# 快速排序的框架,只要完成partition这个归位算法即可。
def quick_sort(data,left,right):
    if left < right:
        # 实际上是一个二叉树的前序遍历的框架
        mid = partition(data,left,right)
        quick_sort(data,left,mid-1)
        quick_sort(data, mid+1, right)

def partition(list,left,right):
    # 相当于是把list[left]即相对的第一位给空出来
    temp = list[left]
    while left < right:
        # 如果序列中没有找到比temp小的数，也就是这个while循环会一直运行，会导致一个问题right终将等于left，这样会导致跳不出最大的循环
        while left < right and temp <= list[right]:
            # 往左走一步
            right -= 1
        #     把右边的值写到左边的空位上
        list[left] = list[right]
        while left < right and temp >= list[left]:
            left += 1
        list[right] = list[left]
    #     最终跳出最大的循环时，left = right，此时再把temp归位
    list[right] = temp
    return right

list = [2,3,9,7,4,6,5]
quick_sort(list,0,6)
print(list)




