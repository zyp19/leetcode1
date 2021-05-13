# /**
# 给定商店每天的营业额,求对于每一天需要等几天才可以等到营业额增加，如果该天之后不存在营业额更多的一天,则记为0.
# Input:[83,84,85,81,79,82,86,83]
# Output:[1,1,4,2,1,1,0,0]
# **/
class Solution:
    def func1(self,list):
        result = []
        for i in range(len(list)-1):
            for j in range(i+1,len(list)):
                if list[j]>list[i]:
                    result.append(j-i)
                    break
        result.append(0)
        return result
solution = Solution()
result = solution.func1([83,84,85,81,79,82,86,83])
print(result)
