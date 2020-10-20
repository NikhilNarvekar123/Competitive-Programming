class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        '''
        i = 0
        j = len(nums) - 1
        m = 0
        
        while i <= j:
            
            m = (j + i) // 2
            
            if(nums[m] == target):
                return m
            elif(nums[m] > target):
                j = m - 1
            elif(nums[m] < target):
                i = m + 1
            

        return i
        '''
    
        
        
        
        
    
        for i in range(len(nums)):
            
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
            if nums[i] < target and i == len(nums) - 1:
                return i + 1
    
