# -*- coding: utf-8 -*-
"""93.复原ip地址
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：
输入：s = "0000"
输出：["0.0.0.0"]
"""
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res ,path = [],[]
        self.backtrack(s,0,path,res)
        return res
    # s和startIndex表示选择列表，path表示路径
    def backtrack(self, s, startIndex, path, res):
        if len(path) > 4:
            return
        if len(path) == 4 and startIndex != len(s):
            return
        if len(path) == 4:
            res.append(".".join(path))
            return
        # 选择in选择列表
        for i in range(startIndex, len(s)):
            # 切分字符串的长度
            newStr = s[startIndex : i+1]
            print(newStr,startIndex,i,path,res)
            # 排除不合法的选择：前置0和长度大于三
            if len(newStr) > 1 and newStr[0] == '0' or len(newStr) > 3:
                break
            num = int(newStr)
            if num<0 or num>255:
                continue
            path.append(newStr)
            self.backtrack(s, i+1, path, res)
            path.pop(-1)
s = Solution()
print(s.restoreIpAddresses(s = "25525511135"))