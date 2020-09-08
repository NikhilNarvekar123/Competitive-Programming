class Solution:
    def romanToInt(self, s: str) -> int:
        
        num = 0
        prev = ''
        
        for c in s:
            if c == 'I':
                num += 1
            elif c == 'V':
                num += 5 if prev != 'I' else 3
            elif c == 'X':
                num += 10 if prev != 'I' else 8
            elif c == 'L':
                num += 50 if prev != 'X' else 30 
            elif c == 'C':
                num += 100 if prev != 'X' else 80
            elif c == 'D':
                num += 500 if prev != 'C' else 300 
            elif c == 'M':
                num += 1000 if prev != 'C' else 800
            prev = c
            
        return num
        
        
        
        
        
    """
        num = 0
        lastnum = 0
        flag = False
        
        for c in s:
            
            if (lastnum == 1 and (c in ['V','X'])) or (lastnum == 10 and (c in ['L','C'])) or (lastnum == 100 and (c in ['D','M'])):
                num += -2 * lastnum
            
            if c == "I":
                num += 1
                lastnum = 1
                flag = True
            elif c == "V":
                num += 5
            elif c == 'X':
                num += 10
                lastnum = 10
                flag = True
            elif c == 'L':
                num += 50
            elif c == 'C':
                num += 100
                lastnum = 100
                flag = True
            elif c == 'D':
                num += 500
            elif c == 'M':
                num += 1000
                
        
        return num
        
        """
