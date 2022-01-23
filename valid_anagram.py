'''
O(n)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        repMap = collections.defaultdict(int)
        
        for i in range(len(s)):
            repMap[s[i]] += 1
            repMap[t[i]] -= 1
        
        for key, val in repMap.items():
            if val != 0:
                return False
        
        return True
