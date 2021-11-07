'''
run-time: 1368 ms (faster than 46.99%)
mem-usage: 14.4 mb (less than 60.42%)
O(n^2)
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ''
        
        def helper(res: str, l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r + 1 - l) > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1
            return res
        
        for i in range(len(s)):
            res = helper(res, i, i)
            res = helper(res, i, i + 1)
        
        return res
