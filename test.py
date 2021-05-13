# 1.字符串转列表
# str3 = "en oo nn"
# list3 = str3.split()和下面的作用一样，结果都是['en', 'oo', 'nn']
# list2 = str3.split(" ")
# list2 = str3.split("")错误的写法，这里面不能为空
# print(list2)
# str1 = 'hello world'
# print(str1.split('这里传任何字符串中没有的分割单位都可以，但是不能为空'))
# print(str1.split(" "))['hello', 'world']
# print(list(str1))['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# 输出：['helloworld']
# version1 = "1.01"
#  version1.split(".")->['1','01']
#  list(map(int,version1.split(".")))->[1,1]

# 2.列表转字符串
# 方法1：拼接
# 方法2："双引号中的内容是拼接列表元素的"join(list)]
# l = ["yes","mola"]
# l = l[0]+l[1]
# print(l)-->yesmola
# l1 = "o".join(l)
# print(l1)-->yesomola
# from collections import Counter
# colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# c = Counter(colors)
# print(c)
# print (dict(c))

# visited = set()
# visited.add([1,2,3])
# print(visited)

# for x in range(ord('a'), ord('z') + 1):
#     print(chr(x))
# n = 2
# target = str(n-1)+str(n-2)+str(n-1)+str(n-1)
# print(target)
grid = [[0,0,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,1],[1,1,1,0,0,0]]
re = ""
for i in range(len(grid)):
    for j in range(len(grid[i])):
        re = re+str(grid[i][j])
print(re)