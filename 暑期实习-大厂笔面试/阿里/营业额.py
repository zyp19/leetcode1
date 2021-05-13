# /**
# 给定商店每天的营业额,求对于每一天需要等几天才可以等到营业额增加，如果该天之后不存在更营业额更多的一天,则记为0.
# Input:[83,84,85,81,79,82,86,83]
# Output:[1,1,4,2,1,1,0,0]
# **/
class Solution:
    def function(self, list):
        result = []
        i,j = 0,0
        while i < len(list)-1:
            j = i + 1
            while j < len(list):
                if list[j] > list[i]:
                    result.append(j-i)
                    i += 1
                    break
                else:
                    j += 1
            else:
                result.append(0)
                i += 1
        if i == len(list)-1:
            result.append(0)
        return result
solution = Solution()
result = solution.function([83, 84, 85, 81, 79, 82, 86, 83])
print(result)