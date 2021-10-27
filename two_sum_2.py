'''
run-time: 64 ms (faster than 76.79%)
mem-usage: 14.6 mb (less than 86.86%)
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            
            numSum = numbers[i] + numbers[j] 
            
            if numSum == target:
                return [i+1,j+1]
            elif numSum > target:
                j -= 1
            else:
                i += 1
            
        return []
