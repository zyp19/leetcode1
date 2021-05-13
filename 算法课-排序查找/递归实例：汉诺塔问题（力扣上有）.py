"""
三、递归
1.2个特点：调用自身、有结束条件
def func1(x):
    print(x)
    func1(x-1) #不是一个递归，因为没有结束的条件
def func2(x)
    if x>0:
        print(x)
        func2(x-1)#表面上有结束条件x>0，但实际上没有
def func3(x)
    if x>0:
        print(x)
        func3(x-1)#输入x=3，打印3，2，1
def func4(x)
    if x>0:
        func4(x-1)
        print(x)#输入x=3，打印1，2，3
四、递归实例：汉诺塔问题
"""
"""面试题 08.06. 汉诺塔问题
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上
(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。
请编写程序，将所有盘子从第一根柱子移到最后一根柱子。
"""
"""
递归思路：
n个盘子时，1.把n-1个圆盘从A经过C移动到B 2.把第n个圆盘从A移动到C 3.把n-1个圆盘从B经过A移动到C

"""
class Solution:
    def hanota(self,n,a,b,c):
        if n>0:
            self.hanota(n-1,a,c,b)
            print("把第n个圆盘从%s移动到%s" %(a,c))
            self.hanota(n-1,b,a,c)
solution = Solution()
solution.hanota(3,"A","B","C")
