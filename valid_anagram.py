'''
run-time: 52 ms (faster than 60.77%)
mem-usage: 14.5 mb (less than 81.61%)
O(n)
'''

class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if len(t) != len(s):
            return False
        
        charMap = {}
        
        for c in s:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1
        
        for c in t:
            if c in charMap:
                charMap[c] -= 1
        
        
        for key, val in charMap.items():
            if val != 0:
                return False
            
        return True
        
