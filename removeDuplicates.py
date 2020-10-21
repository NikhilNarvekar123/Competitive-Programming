class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        i = 0
        for j in range(1, len(nums)):
            if(nums[j] != nums[i]):
                i += 1
                nums[i] = nums[j]
        
        return i + 1
        
        
        
        '''
        i = 0
        j = i + 1
        
        while j <= len(nums) - 1:
            num1 = nums[i]
            num2 = nums[j]
            if(num1 == num2):
                nums.pop(j)
            else:
                i = j
                j += 1
                
        return len(nums)
        
        '''
