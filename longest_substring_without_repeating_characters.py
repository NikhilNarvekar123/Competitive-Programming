'''
run-time: 82 ms, faster than 38.77%
mem-usage: 14.4 mb, less than 54.72%
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        if len(s) == 1 or len(s) == 0:
            return len(s)
        
        characMap = {}
        start = 0
        maxLength = 0
        
        for i in range(len(s)):
            
            if s[i] in characMap and characMap[s[i]] >= start:
                start = characMap[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            
            characMap[s[i]] = i
            
        
        
        return maxLength
