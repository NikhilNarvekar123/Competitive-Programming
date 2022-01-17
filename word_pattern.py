'''
O(n) runtime
O(n) mem
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        i = j = 0
        ref = {}
        words = s.split(' ')
        seenWords = set()

        if len(words) != len(pattern):
            return False        
        
        while i < len(pattern):
            if pattern[i] in ref:
                if ref[pattern[i]] != words[j]:
                    return False
            elif words[j] in seenWords:
                return False
            else:
                seenWords.add(words[j])
                ref[pattern[i]] = words[j]
            i += 1
            j += 1
        
        return True
