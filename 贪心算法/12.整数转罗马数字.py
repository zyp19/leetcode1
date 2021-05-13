"""12.整数转罗马数字
这道题使用贪心算法的直觉来源是：尽可能优先使用较大数值对应的字符，最后转换得到的罗马数字的字符个数更少，字符更少更方便交流使用，这应该是设计
罗马数字的人们的初衷。
可以发现 规律：数字 11、55、1010、5050、100100、500500、10001000 是分水岭，转换的时候默认使用加法，如果一个字符超过 33 次重复使用，
就改成减法，这样就可以用两个字符表示一个罗马数字（数量更少），所以 44 应该看成 5 - 15−1，即 IV。
其实题目中也强调了「做减法的特例」：出现 44、99、4040、9090、400400、900900
贪心思想的思路：因为想获取最短的罗马数字，肯定要贪心地去挑选数值最大地罗马数字，因此就挑选一个最接近num的表中的整数值的对应罗马数字，
每次挑完再减去对应的整数数值，再继续迭代。
代码没处理减法，因为不需要呀，只有4 9 40  90这些需要减法，但是这些4 9 40 90已经自定义到表中了呀
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        res = ''
        while index < 13:
            # 注意：这里是等于号，表示尽量使用大的"面值"
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]
            index += 1
        return res