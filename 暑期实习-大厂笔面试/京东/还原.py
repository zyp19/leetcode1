"""
有一个含有n个数字的序列，每个数字的大小是不超过200的正整数，同时这个序列满足以下条件：
1. a_1<=a_2
2. a_n<=a_(n-1) （此时n>2）
3. a_i<=max(a_{i-1},a_{i+1})
但是很不幸的是，在序列保存的过程中，有些数字丢失了，请你根据上述条件，计算可能有多少种不同的序列可以满足以上条件。
"""
class solution:
    def func(self,list):
        result = []
        m_0 =[]
        for m in list:
            m_0.append(list.index(0))
        for m in m_0:
            for i in range(0,200):
                if m == 0:
                    if list[-2] > list[-1]:
                        return -1
                    else:
                        if list[1] < i:
                            continue
                        else:
                            result.append(i)
                elif m == len(list)-1:
                    if list[1] > list[0]:
                        return -1
                    else:
                        if list[len(list)-2] <= i:
                            continue
                        else:
                            result.append(i)
                else:
                    a = max(list[m-1],list[m+1])
                    if i > a:
                        continue
                    else:
                        result.append(i)

s = solution()
result = s.func([0,5,7])
print(result)



