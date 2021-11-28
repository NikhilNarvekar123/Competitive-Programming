'''
run-time: 64 ms, faster than 62.12%
mem-usage: 14.1 mb, less than 78.41%
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        elif x % 10 == 0 and x != 0:
            return False
        
        reverse = 0
        
        while reverse < x:
            reverse = (reverse * 10) + (x % 10)
            if x > reverse:
                x = x // 10
            else:
                break

        return x == reverse
