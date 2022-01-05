'''
run-time: 353 ms, faster than 63.53%
mem-usage: 14.5 mb, less than 16.74%
O(n)
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxNum = curNum = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                curNum += 1
            else:
                maxNum = max(maxNum, curNum)
                curNum = 0
            
        return max(curNum, maxNum)
        
