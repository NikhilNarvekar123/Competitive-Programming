'''
run-time: 36 ms
mem-usage: 14.2 MB
'''

class Solution(object):
    def twoSum(self, nums, target):
        
        difMap = {}
        
        for i in range(len(nums)):
            if nums[i] in difMap:
                return [difMap[nums[i]], i]
            else:
                difMap[target - nums[i]] = i
        
        return
