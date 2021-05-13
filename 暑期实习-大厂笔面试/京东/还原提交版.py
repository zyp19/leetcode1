def func(len,k,list):
    result = []
    sum,sum_0= 0,0
    for i in range(len-2):
        sum_0 = 0
        j = i
        while j < i+k:
            sum_0 = sum_0 + list[j]
            j += 1
        if sum_0 > sum:
            sum = sum_0
            result.append(j-k)
    return result[-1]+2

while True:
    len,k = map(int, input().split())
    list=[int(i) for i in input().split()]
    re = func(len,k,list)
    print(re)