'''
run-time: 32 ms (faster than 74.06%)
mem-usage: 14.1 mb (less than 85.79%)
dfs/backtracking
'''

class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
    
    

        digitMap = {2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'], 
                    5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z']}
        
        
        def helper(combos, curVal, i):
            
            if i >= len(digits):
                combos.append(curVal)
                return
            
            c = int(digits[i])
            
            for charac in digitMap[c]:
                    
                tempVal = curVal + charac
                helper(combos, tempVal, i + 1)
            
            return combos
                    
        return helper([], '', 0)
