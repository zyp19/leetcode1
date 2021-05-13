"""1239.串联字符串的最大长度
给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
请返回所有可行解 s 中最长长度。
输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
"""
# BFS是求最短、最小的，该题明显不是
# 滑动窗口是求子串 子数组问题 该题较明显不是
# 想不到好用的方法，应该是动规或回溯，由于现在在做BFS专题，所以先等下做
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
