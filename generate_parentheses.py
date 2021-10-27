'''
run-time: 32 ms (faster than 90.64%)
mem-usage: 14.7 mb (less than 39.82%)
'''

class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def backtrack(curStr, numOpen, numClosed):
            
            if numOpen == n == numClosed:
                res.append(curStr)
            
            if numOpen < n:
                backtrack(curStr + '(', numOpen + 1, numClosed)
                
            if numClosed < numOpen: 
                backtrack(curStr + ')', numOpen, numClosed + 1)
            
            
        backtrack('(', 1, 0)
        return res
