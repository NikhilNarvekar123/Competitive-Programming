'''
run-time: 52 ms (faster than 57.69%)
mem-usage: 14.5 mb (less than 80.58%)
O(n)
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] == ' ' or not (s[i].isalpha() or s[i].isdigit()):
                i += 1
            elif s[j] == ' ' or not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
                
        return True
