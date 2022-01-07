'''
run-time: 24 ms, faster than 98.59%
mem-usage: 14.2 mb, less than 76.54%
O(n)
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        i = 0
        n = len(nums)
        
        while(i < n):
            if(nums[i] == val):
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
                
        return n
        
        
        # preserves relative order
        '''
        i = len(nums) - 1
        k = 0
        
        while i >= 0:
            if nums[i] == val:
                k += 1
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
            i -= 1
        
        return len(nums) - k
        '''
        
        
        '''
        for idx in range(len(nums)-1, -1, -1):
            if(nums[idx] == val):
                nums.pop(idx)
                
        return len(nums)
        
        '''
