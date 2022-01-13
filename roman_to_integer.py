'''
O(n)
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbolMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        val = 0
        for i in range(len(s)):
            cur = symbolMap[s[i]]
            if i < len(s) - 1:
                if cur >= symbolMap[s[i + 1]]:
                    val += cur
                else:
                    val -= cur
            else:
                val += cur
        
        return val
        
