class Solution:
    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        if(len(s) == 0 or len(s) == 1):
            return len(s)
        
        charac = set()
        
        i = 0
        j = 0
        maxLength = -1
        
        while(i < len(s) and j < len(s)):
            
            char = s[j]
            
            if char not in charac:
                charac.add(char)
                j += 1
                maxLength = j - i if j - i > maxLength else maxLength 
            else:
                charac.remove(s[i])
                i += 1
        
        return maxLength
        
         
        
#         if(len(s) == 0):
#             return 0
        
#         charac = {}
        
        
#         idx = 0
        
#         length = 0
#         maxLength = -1
        
#         while(idx < len(s)):
            
#             char = s[idx]
            
#             if char not in charac:
#                 length += 1
#                 charac[char] = idx
#             else:
#                 idx = charac[char]
#                 length = 0
#                 charac = {}
        
#             maxLength = length if length > maxLength else maxLength
#             idx += 1
        
#         return maxLength
    
    
    

