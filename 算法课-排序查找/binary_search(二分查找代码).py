"精髓：双指针，将候选区折半"

class Solution:
    def binary_search(self,value,list):
        list.sort()
        l,r = 0,len(list)-1
        while l <= r:
            mid = int((l+r)/2)
            if value == list[mid]:
                return mid
            elif value > list[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1
solution =Solution()
result = solution.binary_search(1,[8,4,1,2,3,2])
print(result)