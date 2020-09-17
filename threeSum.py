class Solution:
    
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        numSet = set()
        rez = []
        
        nums.sort()
        print(nums)
        
        for i in range(0, len(nums)):
            
            y = {nums[i]}
            print()
            print(y)
            
            if numSet.isdisjoint(y) and nums[i] <= 0: 
                k = len(nums) - 1
                j = i + 1
                while not ((k < j) or k == j):
                    numSum = nums[i] + nums[j] + nums[k]
                    if numSum == 0:
                        rez.append([nums[i], nums[j], nums[k]])
                        j += 1
                    elif numSum > 0:
                        k -= 1
                    elif numSum < 0:
                        j += 1
                    
                    print(numSum, end=" ")
            
            numSet.add(nums[i])
            
        return rez
                    
