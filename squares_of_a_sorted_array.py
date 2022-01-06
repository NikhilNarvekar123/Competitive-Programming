'''
run-time: 313 ms, faster than 21.41%
mem-usage: 16.2 mb, less than 31.61%
O(n)
'''

from collections import deque

class Solution:
  
    # more compact approach that uses a deque and works its way inwards
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        res = deque()
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            p1 = nums[i] ** 2
            p2 = nums[j] ** 2
            if p1 >= p2:
                res.appendleft(p1)
                i += 1
            if p1 <= p2 and i <= j:
                res.appendleft(p2)
                j -= 1
                
        return list(res)
  
    # less efficient approach that works its way outwards
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        m = 0
        res = []
        
        while m < len(nums):
            if nums[m] >= 0:
                break
            m += 1
        
        j = m
        i = m - 1
        
        while i >= 0 and j < len(nums):
            p1 = nums[j] ** 2
            p2 = nums[i] ** 2

            if p1 <= p2:
                res.append(p1)
                j += 1
            if p1 >= p2:
                res.append(p2)
                i -= 1
        
        while i >= 0:
            res.append(nums[i] ** 2) 
            i -= 1
        
        while j < len(nums):
            res.append(nums[j] ** 2)
            j += 1
        
        return res

        
