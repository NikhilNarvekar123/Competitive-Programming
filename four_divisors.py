'''
run-time: 521 ms (faster than 71.38%)
mem-usage: 15.5 mb (less than 58.30%)
O(n*m), where m is the average number of inner iterations of the loop (capped at the square root of the number)
'''

import math

class Solution:
    
    def sumFourDivisors(self, nums: List[int]) -> int:
    
        overallSum = 0
    
        for num in nums:
            
            divisorSum = 0
            numDivisors = 0
            n = int(math.sqrt(num)) + 1
            
            for i in range(1, n):
                
                if num % i == 0:
                    j = num // i
                    numDivisors += 2 if j != i else 1
                    divisorSum += i + (num//i)
                
                if numDivisors > 4:
                    break
            
            if numDivisors == 4:
                overallSum += divisorSum 
            
            
        return overallSum
