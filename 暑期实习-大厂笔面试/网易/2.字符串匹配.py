class Solution:
    def getMostStrLength(self , s0 , s1 , cList ):
        flag1 = {}
        flag2 = {}
        num = 0
        for c in s0:
            flag1[c] = flag1.get(c,0) + 1
        #     判断两个字符串的相同部分
        l ,r = 0,0
        while r < len(s1):
            if s1[r] not in flag1:
                l,r = r + 1,r+1
                flag2.clear()
            else:
                flag2[s1[r]]  = flag2.get(s1[r],0)
                # 控制字母的个数
                while flag1[s1[r]] == flag2[s1[r]] and s1[r] not in cList:
                    flag1[s1[l]] -= 1
                    l += 1
                    num -= 1
                    # 当条件满足的时候，就更新（增大）窗口
                flag2[s1[r]] += 1
                r += 1
                num += 1
        return(num)
solution = Solution()
result = solution.getMostStrLength(s0="abc%", s1="zxaab%c%%%", cList = ['#','%'])
print(result)






