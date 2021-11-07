'''
run-time: 92 ms (faster than 93.33%)
mem-usage: 17.1 mb (less than 86.73%)
O(n) pass, but internal sorting procedures take up time
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in groups:
                groups[sortedWord].append(word)
            else:
                groups[sortedWord] = [word]
        
        res = []
        for key, val in groups.items():
            res.append(val)
        
        return res
