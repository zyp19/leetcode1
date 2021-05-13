class Solution:
    def lengthOfLongestSubstring(self, s: str):
        window = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            c = s[r]
            r += 1
            if c in window.keys(): window[c] += 1
            else: window[c] = 1
            while window[c] > 1:
                d = s[l]
                l += 1
                window[d] -= 1
            res = max(r-l, res)
        return res
solution = Solution()
nums = solution.lengthOfLongestSubstring(s = "abcabcbb")
print(nums)
