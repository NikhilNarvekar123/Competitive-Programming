'''
O(n)
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        expected = 0
        for i in range(0, len(nums) + 1):
            expected += i
        
        actual = 0
        for i in range(0, len(nums)):
            actual += nums[i]
            
        return expected - actual
