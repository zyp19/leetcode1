"""88.合并两个有序数组
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。
"""
"""
我写的代码在这里能通过，但是在leetcode上不能全部ac过

"""
class Solution:
    def merge(self, nums1, m, nums2, n) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
        if m == 0 and n == 0:
            return []
        elif m == 0:
            return nums2
        elif n == 0:
            return nums1
        elif m!=0 and n!=0:
            while i <= m and j <= n:
                if nums1[i] < nums2[j]:
                    i += 1
                # 包含了二者相等的情况
                else:
                    a = m
                    while a >= i:
                        nums1[a+1] = nums1[a]
                        a -= 1
                    nums1[i] =nums2[j]
                    j += 1
            while m < i <m+n and j < n:
                nums1[i] =nums2[j]
                i += 1
                j += 1
            return nums1
solution = Solution()
nums1 = solution.merge([0],0,[1],1)
print(nums1)
