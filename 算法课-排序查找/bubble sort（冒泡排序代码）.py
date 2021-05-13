# 时间复杂度(o(n^2))
def bubble_sort(list):
    for i in range(len(list)-1):#趟数
        # j是在无序区中的指针
        exchange = False
        for j in range(len(list)-i-1):
            if list[j+1] < list[j]:
                exchange = True
                list[j],list[j+1] = list[j+1],list[j]
        if exchange == False:
            return
bubble_sort([9,8,7,1,2,3,4,5,6])
