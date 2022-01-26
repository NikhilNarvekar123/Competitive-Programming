'''
O(n)
Works bc XOR is commutative
Basically every pair of duplicates (ex 2 ^ 2) equals 0, and
0 ^ x = x. X is the number that doesn't have a duplicate.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res
        
