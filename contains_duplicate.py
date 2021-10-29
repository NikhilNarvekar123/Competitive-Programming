'''
run-time: 112 ms (faster than 94.89%)
mem-usage: 20.1 mb (less than 64.32%)
O(n)
'''

class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        freqSet = set()
        
        for i in range(len(nums)):
            if nums[i] in freqSet:
                return True
            else:
                freqSet.add(nums[i])
        
        return False
