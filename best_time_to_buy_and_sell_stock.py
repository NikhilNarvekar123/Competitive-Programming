'''
O(n)
Kandane's algo but modified so array being summed is array of differences between consecutive indices
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curSum = 0
        maxSum = 0
        
        for i in range(len(prices) - 1):
            curSum += prices[i + 1] - prices[i]
            if curSum < 0:
                curSum = 0
            maxSum = max(curSum, maxSum)

        return maxSum
