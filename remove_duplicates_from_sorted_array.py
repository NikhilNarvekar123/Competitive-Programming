'''
run-time: 139 ms, faster than 28.82%
mem-usage: 15.6 mb, less than 48.03%
Still O(n) with O(1) mem space
'''

class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        swapIdx = 0
        prevNum = None
        
        for i in range(len(nums)):
            if prevNum != nums[i]:
                if swapIdx != i:
                    nums[swapIdx] = nums[i]
                swapIdx += 1
            prevNum = nums[i]
        
        return swapIdx
