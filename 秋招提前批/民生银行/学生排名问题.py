# t = int(input())
num =[[90,80,68],[91,90,65],[73,90,66],[90,90,66],[90,90,66],[90,80,69]]
# for i in range(t):
#     num.append(list(map(int,input().split(" "))))
def function(num):
    # 二维数组排序
    for i in range(len(num)):
            num[i].append(sum(num[i][0:]))
    print(num)
    bubble_sort(num[0])
    print(num)



def bubble_sort(list):
        for i in range(len(list) - 1):  # 趟数
            # j是在无序区中的指针
            exchange = False
            for j in range(len(list) - i - 1):
                if list[j + 1] < list[j]:
                    exchange = True
                    list[j], list[j + 1] = list[j + 1], list[j]
            if exchange == False:
                return
function(num)