# 1.二维数组的遍历方式
"""
第一种方式:类似于MATLAB中的二维数据索引,比较直观,容易理解
首先,定义了一个二维列表list2d.然后利用一个两层循环遍历这个二维列表.利用range函数限制循环次数,利用len函数获得列表的行数和列数.
注意这两者的不同.
评价:这个方式不够好:
首先,Python中列表和MATLAB中不同,不需要每行的列数相同
利用行列下标索引方式,则必须要求,每行的列数相同.
"""
list2d = [[1,2,3],[4,5,6]]
sum = 0
for i in range(len(list2d)):
    for j in range(len(list2d[0])):
        # i(0,1) j(0,2)
        sum += list2d[i][j]
print(sum)

"""
第二种方式:利用列表句柄
提示:作为新手,一定要熟悉各种数据结构的句柄遍历方式.
"""
list2d = [[1,2,3],[4,5]]
sum = 0
for i in range(len(list2d)):
    for j in range(len(list2d[0])):
        sum += list2d[i][j]
print(sum)

list2d = [[1,2,3],[4,5]]
sum = 0
for i in list2d:
    for j in i:
        sum += j
print(sum)