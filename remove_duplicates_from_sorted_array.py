'''
run-time: 151 ms, faster than 21.81%
mem-usage: 15.6 mb, less than 79.59%
O(n)
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        
        return i + 1
