'''
O(n) run
O(n) mem
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res = set()
        for i in range(1, len(nums) + 1):
            res.add(i)
        
        for n in nums:
            if n in res:
                res.remove(n)
        
        return list(res)
