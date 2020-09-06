class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        complementDict = {}
        for i in range(0, len(nums)):
            complementDict[nums[i]] = i;
        
        for j in range(0, len(nums)):
            complementDict[nums[i]] = i;
            x = target - nums[j]
            a = complementDict.get(x)
            if(a != None and a != j):
                return(j, a)
    
    
    
    
    ''' Old solution (O(n^2))
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]           
    '''
