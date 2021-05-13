""""46.全排列
给定一个不含重复数字的数组nums，返回其所有可能的全排列 。你可以按任意顺序返回答案。
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List
class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 路径
        track = []
        # 存放结果
        self.backtrack(nums,track)
        return self.res
    # 参数为选择列表，路径
    def backtrack(self,nums,track):
        # if满足结束条件
        if len(nums) == len(track):
            self.res.append(track[:])
            return
        # for选择in选择列表
        for i in nums:
#             排除不合法的选择
            if i in track:
                continue
#             做选择
            track.append(i)
            # 进入下一层决策树
            self.backtrack(nums,track)
            # 回退选择
            track.pop(-1)
s = Solution()
print(s.permute([1,2,3]))
