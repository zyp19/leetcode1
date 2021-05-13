# 5.4学的，5.12看的时候就不会了 5.14看会了 6.23又记不清代码的细节了
# 归并排序的归并过程：1.取中点2.分解：左右两边递归两次3.合并两部分
def merge(li,low,mid,high):
    # i是左边数组的起始
    i = low
    # j是右边数组的起始
    j = mid + 1
    ltmp = []
    # 只要两边都有数
    while i <= mid and j <= high:
        if li[i]<li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
#        while执行完了，肯定有一部分没有数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    #    将排好序的列表ltmp写回到li中
    li[low:high+1] = ltmp

# li = [2,4,5,7,1,3,6,8]
# merge(li,0,3,7)
# print(li)

def merge_sort(li,low,high):
    if low < high:
        # 找中点
        mid = (low + high)//2
        # 递归调用merge_sort
        # 左半部分分解（即多层递归），直到每个可归并的元素个数为1
        merge_sort(li,low,mid)
        # 右半部分分解
        merge_sort(li,mid+1,high)
        # 合并两个有序链表
        merge(li,low,mid,high)
li = [2,4,5,7,1,3,6,8]
merge_sort(li,0,7)
print(li)
