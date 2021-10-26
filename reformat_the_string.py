'''
run-time: 44 ms, faster than 80.68%
mem-usage: 14.1 mb, less than 87.78%
O(n)
'''

class Solution:
    def reformat(self, s: str) -> str:
        
        if len(s) == 1:
            return s
        
        nums = []
        alphas = []
        
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                alphas.append(c)
        
        
        if len(nums) == 0 or len(alphas) == 0:
            return ''
        
        if abs(len(nums) - len(alphas)) > 1:
            return ''
        
        res = ''
        outsideArr = alphas if len(alphas) >= len(nums) else nums
        insideArr = alphas if len(alphas) < len(nums) else nums
        
        for i in range(len(outsideArr)):
            res += outsideArr[i]
            if i < len(insideArr):
                res += insideArr[i]
                
        return res
            
        

            
