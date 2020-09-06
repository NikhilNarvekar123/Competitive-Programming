import math as m

class Solution:
    
    
    def reverse(self, x: int) -> int:
    
        rev = 0
        digit = 0
        maxsize = 2147483647
        
        
        while x != 0:
        
            if x < 0:
                digit = x % -10
                x = m.ceil(x / 10)
            else:
                digit = x % 10
                x = x // 10
                
            if rev > maxsize / 10 or (rev == maxsize / 10 and digit > 7):
                return 0 
            if rev < ((-maxsize - 1) / 10) or (rev == ((-maxsize - 1) / 10) and digit < -8):
                return 0
            
            rev = rev * 10 + digit
            
        return rev
        
        
        """
        if x >= 0:
            s = str(x)[::-1]
        else: 
            s = str(x)[1:]
            s = s[::-1]
            s = '-' + s
        
        x = int(s)
        
        if x > pow(2, 31) -1 or x < pow(-2, 31):
            return 0    
        else:
            return x
        """
