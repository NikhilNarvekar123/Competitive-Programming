class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        
        
        '''
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        while x > rev:
            rev = rev * 10 + (x % 10)
            x = x // 10
        
        return rev == x or rev // 10 == x
        '''
        
        '''
        if x < 0:
            return False
        
        rev = 0
        y = x
        
        while y != 0:
            digit = y % 10
            y = y // 10
            rev = rev * 10 + digit
        
        return rev == x
        '''
        
        return str(x) == str(x)[::-1]

        
