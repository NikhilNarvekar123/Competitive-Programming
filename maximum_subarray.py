'''
O(n)
Kandane's Algo
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = -math.inf
        sumSoFar = 0
        
        for i in range(len(nums)):
            sumSoFar += nums[i]
            maxSum = max(sumSoFar, maxSum)
            if sumSoFar < 0:
                sumSoFar = 0
        
        return maxSum
