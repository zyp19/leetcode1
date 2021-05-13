# class Solution:
#     @staticmethod
#     def third(x):
#         return x*x*x
#
#     def sxh(self,m,n):
#         for i in range(m,n):
#             a = Solution.third(i/100)
#             b = Solution.third((i /10) % 10)
#             c = Solution.third(i % 10)
#             r = a+b+c
#             if r == i:
#                 print(i,end='')
#             else:
#                 print("no")
# solution = Solution()
# solution.sxh(100,999)

def find(x):
    a = x % 10
    b = (x // 10) % 10
    c = x // 100
    if x == a * a * a + b * b * b + c * c * c:
        return 1
    else:
        return 0
while True:
    a, b = map(int, input().split())
    flag = 0
    for i in range(a, b + 1):
        if find(i) == 1:
            print(i, end=" ")
            flag = 1
    if flag == 0:
        print("no", end="")
    print()

