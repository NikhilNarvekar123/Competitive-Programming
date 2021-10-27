from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        # expand outwards from each character in single pass
        
        
        res = ''
            
        
        for i in range(len(s)):
            
            
            l = r = i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                
                if (r - l + 1) > len(res):
                    res = s[l: r + 1]
                l -= 1
                r += 1
                
            
            l = i
            r = i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                
                if (r - l + 1) > len(res):
                    res = s[l: r + 1]
                l -= 1
                r += 1
            
            
            
                
                
                
                
                
        return res
                
                
            
            
            
            
        
        
        
        
        
        
        
        
        
        # improved brute force
#         def checkPalindrome(x):
            
#             if len(x) == 1:
#                 return True
            
#             i = 0
#             j = len(x) - 1
#             while i <= j:
#                 if x[i] != x[j]:
#                     return False
#                 i += 1
#                 j -= 1
            
#             return True
            
#         curMax = ''
#         palindromeMap = {}
        
#         for i in range(len(s)):
            
#             temp = s[i]
#             localMax = temp 
            
#             for j in range(i + 1, len(s)):
                
#                 temp += s[j]
                
#                 if temp in palindromeMap or checkPalindrome(temp):
#                     if len(temp) > len(localMax):
#                         localMax = temp
#                     if not (temp in palindromeMap):
#                         palindromeMap[temp] = len(temp)
                    
                    
#             if len(localMax) > len(curMax):
#                 curMax = localMax
                
                
#         return curMax
