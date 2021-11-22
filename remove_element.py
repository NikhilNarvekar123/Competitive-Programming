'''
run-time: 24 ms, faster than 98.60%
mem-usage: 14.2 mb, less than 77.35%
O(n) and O(1) mem space
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        swapIdx = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[swapIdx] = nums[i]
                swapIdx += 1
                
        return swapIdx
