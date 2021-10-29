'''
run-time: 1104 ms (faster than 59.55%)
mem-usage: 25.2 mb (faster than 11.92%)
O(n) algorithm
'''


class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
    
    
        # O(n^2)
        # maxProfit = 0
        # for i in range(len(prices) - 1):            
        #     for j in range(i + 1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j] - prices[i])
        # return maxProfit
        
        # O(n)
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(1, len(prices)):
            minPrice = min(prices[i], minPrice)
            maxProfit = max(prices[i] - minPrice, maxProfit)
        
        return maxProfit
            
            
        
