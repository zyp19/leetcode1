def quick_sort(alist, start, end):
    """快速排序：双指针法。平均时间复杂度O(logN),最差时间复杂度o(N2)
    原理：
    1)设置一个基准值
    2)先从右往左进行遍历，因此是右指针递减，直到找到一个比基准值小的数，注意这里，是把这个比基准值小的数赋值给左指针所在位置的数值，一旦找到这样的值，
    就跳出小循环，因此右指针递减的小循环的条件是(low<high and alist[high]>=anchor)
    3)同理，跳出2）的循环之后，再使左指针递增，直到找到一个比基准值大的数，注意这里，是把这个比基准值大的数赋值给右指针所在位置的数值，一旦找到这样的值，
    就跳出这个小循环，因此左指针递减的小循环的条件是(low<high and alist[low]<anchor)
    4)什么时候不再进行2) 3)两个小循环呢？即当low<high不成立的时候，也就是low>=high的时候，且此时不光要跳出循环还要进行将anchor的值赋值给alist[low]
    5）这样就完成了将基准位置左边的值小于anchor，anchor右边的值都是大于anchor的操作。
    6）再将anchor左边的值进行快速排序，anchor右边的值也进行快速排序即可。



    """
    if start >= end:  # 递归的退出条件
        return
    anchor = alist[start]  # 设定起始的基准元素
    low = start  # low为序列左边在开始位置的由左向右移动的游标
    high = end  # high为序列右边末尾位置的由右向左移动的游标
    while low < high:
        # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
        while low < high and alist[high] >= anchor:
            high -= 1
        alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < anchor:
            low += 1
        alist[high] = alist[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    alist[low] = anchor  # 将基准元素放到该位置,
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后



if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)