'''
O(n/2)
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
    
        def reverse(s, i, j):
            if i >= j:
                return
            s[i], s[j] = s[j], s[i]
            reverse(s, i + 1, j - 1)
        
        reverse(s, 0, len(s) - 1)
        
        # iterative
        '''
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        '''
