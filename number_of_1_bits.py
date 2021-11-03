'''
run-time: 32 ms (faster than 71.53%)
mem-usage: 14 mb (less than 89.14%)
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        oneCount = 0
        
        while n != 0:
            if n % 2 == 1:
                oneCount += 1
            n = n // 2
        
        return oneCount
