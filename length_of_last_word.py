'''
O(n) worst-case
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1
        length = 0
        while i >= 0:
            if s[i] != ' ':
                length += 1
            if length != 0 and s[i] == ' ':
                break
            i -= 1
        
        return length
