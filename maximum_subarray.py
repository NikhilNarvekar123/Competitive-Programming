'''
run-time: 812 ms (faster than 8%)
mem-usage: 28.7 mb (less than 12.56%)
still O(n)
'''

class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        localMax = 0
        globalMax = None
        
        for i in range(len(nums)):
            localMax = max(nums[i], nums[i] + localMax)
            if globalMax == None:
                globalMax = localMax
            else:
                globalMax = max(localMax, globalMax)
            
        return globalMax
