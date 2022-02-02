'''
O(n^2) -> Finding all combinations requires n^2 time
'''

class Solution:
    
    def maxLength(self, arr: List[str]) -> int:
    
        combos = [set()]
        maxCombo = 0
        
        for word in arr:
            
            if len(set(word)) != len(word):
                continue
            
            for i in range(len(combos)):
                if len(set(word) & combos[i]) != 0:
                    continue
                combos.append(combos[i] | set(word))
                maxCombo = max(maxCombo, len(combos[-1]))
        
        return maxCombo
