class Solution:
    def isValid(self, s: str) -> bool:

        
        stack = []
        
        mapping  = {')' : '(', ']' : '[', '}' : '{' } 
        
        
        for i in range(0, len(s)):
            
            if(len(stack) == 0):
                stack.append(s[i])
            elif(s[i] in mapping and mapping[s[i]] == stack[-1]):
                stack.pop()
            else:
                stack.append(s[i])
        
        
        if(len(stack) == 0):
            return True
        else:
            return False
    
        
        
        
        
        
        
        '''
    def parity(self, s1: str, s2:str) -> bool:
        if(s1 == '(' and s2 == ')'):
            return True
        if(s1 == '[' and s2 == ']'):
            return True
        if(s1 == '{' and s2 == '}'):
            return True
        return False

        i = 0
        j = 1
        
        
        curBack = ''
        curFront = ''
        valid = False
        
        while(j < len(s)):
            curBack = s[i]
            curFront = s[j]
            
            print(curBack, curFront)
            valid = self.parity(curBack, curFront) 
            if(valid):
                if(j - i % 2 != 0):
                    if(j - i == 1):
                        i += 2
                        j += 2
                    else:
                        i += 1
                        j = i + 1
                else:
                    return False
            else:
                j += 1
                
                
                
                
                
        return valid
    '''
