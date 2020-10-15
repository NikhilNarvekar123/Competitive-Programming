class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        if(len(needle) == 0):
            return 0
        
        
        for i in range(len(haystack) - len(needle) + 1):
            
            if(haystack[i:i+ len(needle)] == needle):
                return i
        
        return -1
        
        
        
        '''
        if len(needle) == 0:
            return 0
        
        
        for i in range(0, len(haystack) - len(needle) + 1):
            
            if(haystack[i] == needle[0]):
                temp = ""
                for j in range(i, i + len(needle)):
                    temp += haystack[j]
                if(temp == needle):
                    return i
        
        return -1
        '''
