'''
Vertical Scanning
O(S) - Single Pass but worst-case scans every character of every string
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort(key=lambda x: len(x))
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            if strs[i][0 : len(prefix)] == prefix:
                continue
            else:
                j = 0
                for c in prefix:
                    if strs[i][j] != c:
                        break
                    else:
                        j += 1
                if j == 0:
                    return ''
                prefix = strs[i][0 : j]
        
        return prefix
