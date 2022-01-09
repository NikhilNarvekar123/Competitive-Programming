'''
O(n)
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        i = 0 if nums[0] == 0 else 1
        
        for j in range(1, len(nums)):
            if nums[j] != 0:
                if nums[i] == 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                i += 1
