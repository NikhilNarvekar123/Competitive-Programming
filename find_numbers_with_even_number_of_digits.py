'''
run-time: 60 ms, faster than 34.14%
mem-usage: 14.2 mb, less than 73.10%
'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0
        
        for num in nums:
            
            digits = 0
            while num != 0:
                num = num // 10
                digits += 1
            
            count += 1 if (digits % 2 == 0) else 0
        
        return count
