'''
O(n^2)
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest = None
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                ts = nums[l] + nums[r] + nums[i]
                if closest == None or abs(target - ts) < abs(target - closest):
                    closest = ts
                    if target - closest == 0:
                        return closest
                elif ts > target:
                    r -= 1
                else:
                    l += 1
        
        return closest
