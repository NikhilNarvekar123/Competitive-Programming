def threeSumClosest(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_target = float("inf")
        for i in range(len(nums)-2):
            for l in range(i+1,len(nums)-1):
                for r in range(l+1,len(nums)):
                    if abs(nums[i] + nums[l] + nums[r] - target) <= abs(min_target):
                        min_target = nums[i] + nums[l] + nums[r] -target
        return min_target + target
